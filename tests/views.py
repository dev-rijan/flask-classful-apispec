from flask_classful import FlaskView, route
from .schemas import PetSchema

pets = [
    {'id': 0, 'name': 'Kitty', 'category': 'cat'},
    {'id': 1, 'name': 'Coco', 'category': 'dog'}
]


class PetView(FlaskView):
    def index(self):
        """Get all pet lists
        ---
        tags:
          - pets
        description: Get all pets
        responses:
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    pets:
                        type: array
                        items: PetSchema
        """
        return PetSchema(many=True).dumps(pets)

    def get(self, id):
        """Get single pet Resource
        ---
        tags:
          - pets
        description: Get pet
        parameters:
        - name: "id"
          in: "path"
          description: "id of required pet"
          required: true
          type: "int"
        responses:
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    pet: PetSchema
        """

        return PetSchema().dumps(pets[0])

    def post(self):
        """Create pet Resource
        ---
        tags:
          - pets
        description: Create Pet
        requestBody:
          content:
            application/json:
              schema: PetSchema
        responses:
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    pet: PetSchema
        """

        return PetSchema(many=True).dumps(pets[0])

    def put(self, id):
        """Custom Pet Resource
        ---
        tags:
          - pets
        description: Custom Pet route
        parameters:
        - name: "id"
          in: "path"
          description: "id of required pet"
          required: true
          type: "int"
        requestBody:
          content:
            application/json:
              schema: PetSchema
        responses:
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    Pet: PetSchema
        """

        return PetSchema(many=True).dumps(pets[0])

    def delete(self, id):
        """Update Pet Resource
        ---
        tags:
          - pets
        description: delete Pet
        parameters:
        - name: "id"
          in: "path"
          description: "id of required pet"
          required: true
          type: "int"

        responses:
          204:
            description: Successfully deleted pet

        """
        return 204

    @route('/custom_route')
    def custom_route(self):
        """Custom pet route
        ---
        tags:
          - pets
        description: custom pet routes
        responses:
          200:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    pets:
                        type: array
                        items: PetSchema
        """
        return PetSchema(many=True).dumps(pets)

    def _not_registered_route(self):
        """
        Not registered routes
        """
        return PetSchema(many=True).dumps(pets)
