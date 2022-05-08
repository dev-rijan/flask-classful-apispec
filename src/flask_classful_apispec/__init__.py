import pkg_resources

__version__ = str(
    pkg_resources.get_distribution("flask-classful-apispec").parsed_version
)
