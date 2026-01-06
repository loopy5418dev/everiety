from flask import Blueprint, request, jsonify, abort

bp = Blueprint("index", __name__)

@bp.route("/", methods=["GET"])
def index():
    return abort(500)