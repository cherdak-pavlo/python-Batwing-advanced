import http

from flask import Blueprint, request, jsonify

from db.db import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    users = db.get_all()
    return jsonify(users)


@book_router.route('/<string:id>')
def retrieve(id):
    book = db.retrieve_by_id(id)
    return book if not str else book, http.HTTPStatus.BAD_REQUEST


@book_router.route('', methods=['POST'])
def create():
    id = request.json.get("id")
    author = request.json.get("author")
    name = request.json.get("name")
    new_book = db.add(id, author, name)
    return new_book if not str else new_book, http.HTTPStatus.BAD_REQUEST


@book_router.route('', methods=['PUT'])
def update():
    id = request.json.get("id")
    author = request.json.get("author")
    name = request.json.get("name")
    update_book = db.update_by_id(id, author, name)
    return update_book if not str else update_book, http.HTTPStatus.BAD_REQUEST


@book_router.route('/<string:id>', methods=['DELETE'])
def delete(id):
    db.delete_by_id(id)
    return {}, http.HTTPStatus.NO_CONTENT
