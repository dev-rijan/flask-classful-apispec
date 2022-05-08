from apispec import APISpec as BaseAPISpec
from apispec.core import Components
from apispec.utils import OpenAPIVersion
from collections import OrderedDict
from flask_classful import FlaskView, get_interesting_members


class APISpec(BaseAPISpec):
    def __init__(self, app=None, plugins=(), **options):
        if app is not None:
            self.init_app(app, plugins=plugins, **options)

    def init_app(self, app, plugins=(), **options):
        self.title = app.config['DOC_TITLE']
        self.version = app.config['DOC_VERSION']
        self.openapi_version = OpenAPIVersion(app.config['DOC_OPEN_API_VERSION'])
        self.options = options
        self.plugins = plugins

        # Metadata
        self._tags = []
        self._paths = OrderedDict()

        # Components
        self.components = Components(self.plugins, self.openapi_version)

        # Plugins
        for plugin in self.plugins:
            plugin.init_spec(self)

    def paths(self, view, app):
        members = get_interesting_members(FlaskView, view)

        for name, value in members:
            endpoint = view.build_route_name(name)

            if hasattr(value, "_rule_cache") and name in value._rule_cache:
                for idx, cached_rule in enumerate(value._rule_cache[name]):
                    rule, options = cached_rule
                    sub, ep, options = view.parse_options(options)
                    endpoint = ep or endpoint
                    print(app.url_map._rules_by_endpoint[endpoint])
                    rule = app.url_map._rules_by_endpoint[endpoint][0]
                    methods = options.get('methods', ['GET'])
                    self.path(path=rule, methods=methods, fun=value)

            elif name in view.special_methods:
                methods = view.special_methods[name]
                endpoint = view.build_route_name(name)
                rule = app.url_map._rules_by_endpoint[endpoint][0]
                self.path(path=rule, methods=methods, fun=value)
            else:
                methods = getattr(view, 'default_methods', ["GET"])
                endpoint = view.build_route_name(name)
                rule = app.url_map._rules_by_endpoint[endpoint][0]
                self.path(path=rule, methods=methods, fun=value)


