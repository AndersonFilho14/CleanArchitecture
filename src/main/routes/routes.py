from flask import Blueprint, request, jsonify


from src.errors.erros_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.validators.user_finder_validator import user_finder_validator
from src.main.composers.user_finder_composer import user_finder_composer
from src.validators.user_register_validator import user_register_validator
from src.main.composers.user_register_composer import user_register_composer

user_rout_bp = Blueprint("user_routes", __name__)

@user_rout_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = None

    try:
        http_response = user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_rout_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None

    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)


    return jsonify(http_response.body), http_response.status_code
