import http
from flask import Blueprint, jsonify, request
from models.books_authors import BooksAuthors
from models.books import Books
from models.authors import Authors
from postgresdb import db
from serializers.books_authors import BooksAuthorsSchema

books_authors = Blueprint("books_authors", __name__, url_prefix='/books_authors')


# ba - booksauthors


@books_authors.route('')
def get():
    ba_all = BooksAuthors.query.all()
    ba_json = BooksAuthorsSchema().dump(ba_all, many=True)
    return jsonify(ba_json)


@books_authors.route('/<int:id_>')
def retrieve(id_):
    ba = BooksAuthors.query.filter_by(id=id_).first()
    ba_json = BooksAuthorsSchema().dump(ba)
    return jsonify(ba_json)


@books_authors.route('/<int:book_id>/<int:author_id>', methods=['POST'])
def create(book_id, author_id):
    if Books.query.filter(Books.id == book_id).first() and Authors.query.filter(Authors.id == author_id).first():
        new_relation = BooksAuthors(book_id=book_id, author_id=author_id)
        db.session.add(new_relation)
        db.session.commit()
        new_relation_json = BooksAuthorsSchema().dump(new_relation)
        return jsonify(new_relation_json), http.HTTPStatus.CREATED
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@books_authors.route('', methods=['PUT'])
def update():
    data = request.get_json(force=True)

    if ba := BooksAuthors.query.filter_by(id=data["id"]).first():
        ba.book_id, ba.author_id = data["book_id"], data["author_id"]
        db.session.add(ba)
        db.session.commit()
        new_ba = BooksAuthorsSchema().dump(ba)
        return jsonify(new_ba)
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@books_authors.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    BooksAuthors.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
