from marshmallow import Schema, fields, validate


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name_book = fields.String(required=True, validate=validate.Length(min=2, max=300))
    year_manufacture = fields.Integer(required=True)
