from marshmallow import Schema, fields


class BooksSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    book_name = fields.String(required=True)
    year = fields.Integer(required=True)
