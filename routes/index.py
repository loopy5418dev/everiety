from flask import Blueprint, request, jsonify, abort, render_template

bp = Blueprint("index", __name__)

common_uas = ["Mozilla", "AppleWebKit", "Gecko"]
@bp.route("/", methods=["GET"])
def index():
    ua = request.headers.get("User-Agent", "")
    if any(s in ua for s in common_uas):
        return render_template("index.html")
    else:
        return jsonify({
            "message": "Fetch the URL listed to get a json containing every endpoint and their information.",
            "link": "https://gist.githubusercontent.com/loopy5418/479de0364e71e1809fc31cebbec88991/raw/everietyEndpointData.json"
        })