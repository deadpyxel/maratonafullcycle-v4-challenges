from flask import jsonify, request

from app import app


@app.route("/", methods=["GET"])
def index():
    req_format = request.args.get("format")
    if req_format == "json":
        return jsonify({"message": "Eu sou Full Cycle"})
    return "Eu sou Full Cycle"
