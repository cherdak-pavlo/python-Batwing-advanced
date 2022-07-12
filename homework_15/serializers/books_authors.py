from marshmallow import Schema, fields
from serializers.books import BooksSchema
from serializers.authors import AuthorsSchema


class BooksAuthorsSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    authors = fields.Nested(AuthorsSchema())
    books = fields.Nested(BooksSchema())
