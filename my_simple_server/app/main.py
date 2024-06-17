# app/main.py

from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)


@main.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    return jsonify({"message": "This is a GET endpoint"}), 200


@main.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.json
    return jsonify({"message": "This is a POST endpoint", "data_received": data}), 200
