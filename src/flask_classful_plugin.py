import re

from flask import current_app
from flask.views import MethodView

from apispec import BasePlugin, yaml_utils
from apispec.exceptions import APISpecError
from flask_classful import FlaskView, get_interesting_members


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

    def path_helper(self, operations, *, path=None, methods=[], fun=None, app=None, **kwargs):
        """Path helper that allows passing a Flask view function."""
        # operations.update(yaml_utils.load_operations_from_docstring(view.__doc__))

        for method in methods:
            method_name = method.lower()
            operations[method_name] = yaml_utils.load_yaml_from_docstring(
                        fun.__doc__
                    )

        return self.flaskpath2openapi(str(path))
