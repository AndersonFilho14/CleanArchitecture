from flask import Blueprint, request, jsonify

from src.main.adapters.request_adapter import request_adapter

user_rout_bp = Blueprint("user_routes", __name__)

@user_route_bd.route("/user/finnd", methods=['GET'])
def