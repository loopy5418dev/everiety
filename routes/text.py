from flask import Blueprint, request, jsonify
import re
import unidecode
from . import errors as err

bp = Blueprint("text", __name__)

@bp.route("/text", methods=["GET"])
def textutils():
    text = request.args.get("text", "")
    if not text:
        return err.missingArgs("text")
    elif len(text) >= 512:
        return jsonify({"error": "argument 'text' is too large, please provide less than 512 characters", "code": "ERR_INPUT_TOO_LARGE"}), 400
    return jsonify({"original": text,
                    "uppercase": text.upper(),
                    "lowercase": text.lower(),
                    "titlecase": text.title(),
                    "reversed": text[::-1],
                    "slugified": re.sub(r'[\W_]+', '-', unidecode.unidecode(text).lower()),
                    "info": {
                        "charcount": len(text),
                        "wordcount": len(text.split()),
                        "bytesize": len(text.encode('utf-8'))
                    }})
    