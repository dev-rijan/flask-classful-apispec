from copy import deepcopy
from apispec import APISpec as BaseAPISpec, yaml_utils
from apispec.core import Components
from apispec.utils import OpenAPIVersion
from collections import OrderedDict
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_classful import FlaskView, get_interesting_members
from flask_classful_apispec.flask_classful_plugin import FlaskClassfulPlugin


class APISpec(BaseAPISpec):
    def __init__(self, app=None, plugins=(), **options):
        if app is not None:
            self.init_app(app, plugins=plugins, **options)

    def init_app(self, app, **options):
        self.title = app.config['DOC_TITLE']
        self.version = app.config['DOC_VERSION']
        self.openapi_version = OpenAPIVersion(app.config['DOC_OPEN_API_VERSION'])
        self.options = options
        self.plugins = (MarshmallowPlugin(), FlaskClassfulPlugin())

        # Metadata
        self._tags = []
        self._paths = OrderedDict()

        # Components
        self.components = Components(self.plugins, self.openapi_version)

        # Plugins
        for plugin in self.plugins:
            plugin.init_spec(self)

    def paths(self, view, app, operations=None):
        members = get_interesting_members(FlaskView, view)
        operations = deepcopy(operations) or OrderedDict()
        operations.update(yaml_utils.load_operations_from_docstring(view.__doc__))

        for member in members:
            self.path(operations=operations, view=view, view_member=member)
