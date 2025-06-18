from flask import Blueprint
from core.db.models import get_user_collection
from core.db.schemas import user_schema, user_partial_schema
from core.utils import format_response, handle_validation
from core.services.user_service import UserService

user_bp = Blueprint("user", __name__)
users= UserService(get_user_collection())

@user_bp.route("/<id>", methods=["GET"])
def fetch_user(id):
    user = users.get_by_id(id)
    return format_response(data=user)

@user_bp.route("/", methods=["GET"])
def fetch_all_users():
    all_users = users.get_all()
    return format_response(data=all_users)

@user_bp.route("/", methods=["POST"])
@handle_validation(user_schema)
def add_user(user_data):
    user_id = users.create(user_data)
    return format_response(data={"id": user_id}, status=201)

@user_bp.route("/<id>", methods=["PUT"])
@handle_validation(user_partial_schema)
def update_user(user_data, id):
    users.update(id, user_data)
    return format_response(message="User updated")

@user_bp.route("/<id>", methods=["DELETE"])
def remove_user(id):
    users.delete(id)
    return format_response(message="User deleted")
