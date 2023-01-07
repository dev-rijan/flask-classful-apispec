import pytest
from flask import Flask
from flask_classful_apispec import APISpec


@pytest.fixture()
def spec(app):
    return APISpec(app)


@pytest.fixture()
def app():
    _app = Flask(__name__)
    _app.config["DOC_TITLE"] = "Swagger petstore"
    _app.config["DOC_VERSION"] = "0.1.1"
    _app.config["DOC_OPEN_API_VERSION"] = "3.0.2"

    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()
