from flask import Blueprint
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError
from pymongo.errors import DuplicateKeyError

from core.utils import format_response

errors_bp = Blueprint("errors", __name__)

@errors_bp.app_errorhandler(HTTPException)
def handle_http_exception(e):
    return format_response(message=e.description, status=e.code)

@errors_bp.app_errorhandler(ValidationError)
def handle_validation_error(e):
    return format_response(data=e.messages, status=400)

@errors_bp.app_errorhandler(ValueError)
def handle_value_error(e):
    return format_response(message=str(e), status=400)

@errors_bp.app_errorhandler(DuplicateKeyError)
def handle_duplicate_key_error(e):
    return format_response(message="Duplicate key error", status=400)

# A catch all for any unhandled exceptions
@errors_bp.app_errorhandler(Exception)
def handle_unexpected_error(e):
    return format_response(message="An unexpected error occurred", status=500)
