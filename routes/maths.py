from flask import Blueprint, request, jsonify, abort

bp = Blueprint("math", __name__)

@bp.route("/math/factorial", methods=["GET"])
def mathutils():
    num = request.args.get("number")
    if not num.isdigit():
        return 