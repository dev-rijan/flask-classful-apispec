Flask classful apispec
======================

A pluggable API specification generator generator for `Flask classful <https://github.com/teracyhq/flask-classful>`_ based on `apispec <https://github.com/jmcarp/flask-apispec>`_

Features
========
- Utilities for parsing flask classful docstrings
- Support for `marshmallow <https://marshmallow.readthedocs.io/>`_

Installation
============

::

    $ pip install flask-classful-apispec

Usage
===================

.. code-block:: python

    import json
    from flask import Flask
    from flask_classful import FlaskView
    from flask_classful_apispec import APISpec
    from marshmallow import Schema, fields
    
    app = Flask(__name__)

    app.config["DOC_TITLE"] = "Swagger petstore"
    app.config["DOC_VERSION"] = "0.1.1"
    app.config["DOC_OPEN_API_VERSION"] = "3.0.2"

    spec = APISpec(app)

    pets = [
        {'id': 0, 'name': 'Kitty', 'category': 'cat'},
        {'id': 1, 'name': 'Coco', 'category': 'dog'}
    ]

    class PetSchema(Schema):
        id = fields.Integer()
        name = fields.String()
        category = fields.String()

    class PetView(FlaskView):
        def index(self):
            """A pet api endpoint.
            ---
            description: Get a list of pets
            responses:
              200:
                schema: PetSchema
            """
            return PetSchema(many=True).dumps(pets)

    PetView.register(app)

    with app.test_request_context():
    spec.paths(PetView, app)
    print(json.dumps(spec.to_dict(), indent=2))

    if __name__ == "__main__":
        app.run()

Generated OpenAPI Spec
======
.. code-block:: json

    {
      "paths": {
        "/pet/": {
          "get": {
            "description": "Get a list of pets",
            "responses": {
              "200": {
                "schema": {
                  "$ref": "#/components/schemas/Pet"
                }
              }
            }
          }
        }
      },
      "info": {
        "title": "Swagger petstore",
        "version": "0.1.1"
      },
      "openapi": "3.0.2",
      "components": {
        "schemas": {
          "Pet": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "category": {
                "type": "string"
              }
            }
          }
        }
      }
    }

