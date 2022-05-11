import pkg_resources
from .api_spec import APISpec
from .flask_classful_plugin import FlaskClassfulPlugin

__version__ = str(
    pkg_resources.get_distribution("flask-classful-apispec").parsed_version
)
__all__ = ['APISpec', 'FlaskClassfulPlugin']
