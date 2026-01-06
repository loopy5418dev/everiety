from flask import Blueprint, request, jsonify, abort
import math

bp = Blueprint("maths", __name__)

@bp.route("/math/factorial", methods=["GET"])
def factorial():
    num = request.args.get("number", "")
    if not num:
        return jsonify({"error": "argument 'number' is required"}), 400
    elif not num.isdigit():
        return jsonify({"error": "argument 'number' must be a valid positive integer"}), 400
    num = int(num)
    return jsonify({
        "original": num,
        "factorial": math.factorial(num)
    })