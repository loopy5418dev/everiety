from flask import Blueprint, jsonify

bp = Blueprint("errors", __name__)

def missingArgs(missingargs):
    if isinstance(missingargs, str):
        missingargs = [missingargs]
    return jsonify({"error": f"missing required argument(s): {", ".join(missingargs)}", "code": "ERR_MISSING_ARGS"}), 400
    
def invalidArg(invarg, type):
    return jsonify({"error": f"invalid argument: {invarg} must be a(n) {type}", "code": "ERR_INVALID_ARG"}), 400
    
@bp.app_errorhandler(404)
def not_found(e):
    return jsonify({"error": "not found: this path/endpoint does not exist. maybe you misspelled something?", "code": "ERR_UNKNOWN_PATH"}), 404

@bp.app_errorhandler(400)
def bad_request(e):
    return jsonify(error="bad request: there's something wrong with your http request content.", code="ERR_UNHANDLED_BAD_REQUEST"), 400

@bp.app_errorhandler(500)
def internal_error(e):
    return jsonify(error="internal server error: something went wrong on our side, try again later", code="ERR_INTERNAL_SE"), 500
    
