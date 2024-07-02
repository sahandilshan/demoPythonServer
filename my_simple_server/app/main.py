# app/main.py

from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)


@main.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    try:
        with open('my_simple_server/app/resources/testFile', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": content}), 200


@main.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.json
    return jsonify({"message": "This is a POST endpoint", "data_received": data}), 200
