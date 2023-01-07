from marshmallow import fields, Schema


class PetSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    category = fields.String()
