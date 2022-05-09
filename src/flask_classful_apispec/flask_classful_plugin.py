import re
from flask import current_app
from apispec import BasePlugin, yaml_utils
from flask_classful import FlaskView


# from flask-restplus
RE_URL = re.compile(r"<(?:[^:<>]+:)?([^<>]+)>")


class FlaskClassfulPlugin(BasePlugin):
    """APISpec plugin for Flask"""

    @staticmethod
    def flaskpath2openapi(path):
        """Convert a Flask URL rule to an OpenAPI-compliant path.

        :param str path: Flask path template.
        """

        return RE_URL.sub(r"{\1}", path)

    def path_helper(self, operations, *, view, app=None, **kwargs):
        """Path helper that allows passing a Flask view function."""
        if app is None:
            app = current_app
        name, value = view

        if hasattr(value, "_rule_cache") and name in value._rule_cache:
            for idx, cached_rule in enumerate(value._rule_cache[name]):
                rule, options = cached_rule
                sub, ep, options = FlaskView.parse_options(options)
                endpoint = ep or endpoint
                print(app.url_map._rules_by_endpoint[endpoint])
                rule = app.url_map._rules_by_endpoint[endpoint][0]
                methods = options.get('methods', ['GET'])

                self._load_docstring(view, operations, methods)
                return self.flaskpath2openapi(str(rule))

        if name in FlaskView.special_methods:
            methods = FlaskView.special_methods[name]
            endpoint = FlaskView.build_route_name(name)
            rule = app.url_map._rules_by_endpoint[endpoint][0]

            self._load_docstring(view, operations, methods)
            return self.flaskpath2openapi(str(rule))

        methods = getattr(FlaskView, 'default_methods', ["GET"])
        endpoint = FlaskView.build_route_name(name)
        rule = app.url_map._rules_by_endpoint[endpoint][0]
        self._load_docstring(view, operations, methods)

        return self.flaskpath2openapi(str(rule))

    def _load_docstring(self, view, operations, methods) -> None:
        for method in methods:
            method_name = method.lower()
            operations[method_name] = yaml_utils.load_yaml_from_docstring(
                view.__doc__
            )
