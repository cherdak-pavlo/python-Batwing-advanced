from flask import Blueprint
from user.serializer import UserSerializer

from core.auth import token_required

user_router = Blueprint("user", __name__, url_prefix="/user")


@user_router.route("/profile")
@token_required
def profile(user):
    schema = UserSerializer()
    profile_json = schema.dump(user)
    return profile_json
