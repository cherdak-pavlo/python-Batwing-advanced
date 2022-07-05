import http
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.book import Book
from serializers.book import BookSchema
from database import db

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def get():
    books = Book.query.order_by(Book.id)
    book_dump = BookSchema().dump(books, many=True)
    return jsonify(book_dump)


@book_router.route('/<int:id_>')
def retrieve(id_):
    searched_book = Book.query.filter(Book.id == id_).first()
    searched_book_dump = BookSchema().dump(searched_book)
    return jsonify(searched_book_dump)


@book_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    try:
        book = BookSchema().load(data)
        db.session.add(Book(name_book=book['name_book'], year_manufacture=book['year_manufacture']))
        db.session.commit()
        book_dump = BookSchema().dump(book)

    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(book_dump)


@book_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    try:
        book = BookSchema().load(data)
        find_book = Book.query.filter_by(id=id_).first()
        find_book.name_book = book['name_book']
        find_book.year_manufacture = book['year_manufacture']
        db.session.add(find_book)
        db.session.commit()
        book_dump = BookSchema().dump(book)

    except ValidationError as e:
        return {'Errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(book_dump)


@book_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Book.query.filter(Book.id == id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
