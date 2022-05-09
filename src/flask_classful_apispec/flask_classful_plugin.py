import re
from typing import Callable, Dict, List, Type, Tuple
from flask import current_app
from apispec import BasePlugin, yaml_utils
from flask_classful import FlaskView


# from flask-restplus
RE_URL = re.compile(r"<(?:[^:<>]+:)?([^<>]+)>")


class FlaskClassfulPlugin(BasePlugin):
    """APISpec plugin for Flask classful"""

    @staticmethod
    def flaskpath2openapi(path):
        """Convert a Flask URL rule to an OpenAPI-compliant path.

        :param str path: Flask path template.
        """

        return RE_URL.sub(r"{\1}", path)

    def path_helper(self, operations: Dict, *, view: Type[FlaskView], view_member: Tuple, app=None, **kwargs) -> str:
        """Path helper that allows parsing a Flask classful method."""
        if app is None:
            app = current_app
        name, value = view_member
        endpoint = view.build_route_name(name)

        if hasattr(value, "_rule_cache") and name in value._rule_cache:
            for cached_rule in value._rule_cache[name]:
                rule, options = cached_rule
                sub, ep, options = view.parse_options(options)
                endpoint = ep or endpoint
                rule = app.url_map._rules_by_endpoint[endpoint][0]
                methods = options.get('methods', ['GET'])

                self._load_docstring(value, operations, methods)
                return self.flaskpath2openapi(str(rule))

        if name in view.special_methods:
            methods = view.special_methods[name]
            rule = app.url_map._rules_by_endpoint[endpoint][0]

            self._load_docstring(value, operations, methods)
            return self.flaskpath2openapi(str(rule))

        methods = getattr(view, 'default_methods', ["GET"])
        rule = app.url_map._rules_by_endpoint[endpoint][0]
        self._load_docstring(value, operations, methods)

        return self.flaskpath2openapi(str(rule))

    def _load_docstring(self, view_member: Callable, operations: Dict, methods: List) -> None:
        for method in methods:
            method_name = method.lower()
            operations[method_name] = yaml_utils.load_yaml_from_docstring(
                view_member.__doc__
            )
