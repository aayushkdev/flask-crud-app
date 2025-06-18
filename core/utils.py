from bson.objectid import ObjectId
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError
from functools import wraps
from flask import request

def validate_object_id(id_str):
    try:
        return ObjectId(id_str)
    except Exception:
        raise BadRequest("Invalid user ID format")


def format_response(data=None, message=None, status=200):
    response = {}
    if message:
        response["message"] = message
    if data is not None:
        response["data"] = data
    return response, status

# Validates input using the schema so no malformed inputs are injected in the db
def handle_validation(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            data = schema.load(request.json)
            return f(data, *args, **kwargs)
        return wrapper
    return decorator
