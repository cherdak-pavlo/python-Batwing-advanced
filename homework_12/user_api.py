import http

from flask import Blueprint, Response, request

from db.db import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    # return jsonify(users)
    # return make_response(jsonify(users), http.HTTPStatus.OK, {"custom": "header"})
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user if not str else user, http.HTTPStatus.BAD_REQUEST


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)
    return new_user if not str else new_user, http.HTTPStatus.BAD_REQUEST


@user_router.route('', methods=['PUT'])
def update():
    email = request.json.get("email")
    name = request.json.get("name")
    password = request.json.get("password")
    update_user = db.update_by_email(email, name, password)
    return update_user if not str else update_user, http.HTTPStatus.BAD_REQUEST


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
