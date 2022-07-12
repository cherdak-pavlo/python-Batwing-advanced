from marshmallow import Schema, fields


class AuthorsSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name_surname = fields.String(required=True)

