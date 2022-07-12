import http
from flask import Blueprint, jsonify, request
from models.books import Books
from serializers.books import BooksSchema
from postgresdb import db
from marshmallow import ValidationError

books_router = Blueprint('books', __name__, url_prefix='/books')


@books_router.route('')
def get():
    all_books = Books.query.all()
    books_json = BooksSchema().dump(all_books, many=True)
    return jsonify(books_json), http.HTTPStatus.OK


@books_router.route('/<int:id_>')
def retrieve(id_):
    book = Books.query.filter(Books.id == id_).first()
    book_json = BooksSchema().dump(book)
    return jsonify(book_json), http.HTTPStatus.OK


@books_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)
    try:
        data_json = BooksSchema().load(data)
        new_book = Books(book_name=data_json["book_name"], year=data_json["year"])
        db.session.add(new_book)
        db.session.commit()
        new_book_json = BooksSchema().dump(new_book)
    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY
    return jsonify(new_book_json), http.HTTPStatus.CREATED


@books_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Books.query.filter(Books.id == id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


@books_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)
    try:
        data_json = BooksSchema().load(data)
        book = Books.query.filter(Books.id == id_).first()
        book.book_name, book.year = data_json["book_name"], data_json["year"]
        db.session.add(book)
        db.session.commit()
        new_book_json = BooksSchema().dump(book)
    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(new_book_json), http.HTTPStatus.OK
