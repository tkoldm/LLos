from flask import Blueprint, request, jsonify
from Service import Service
import json

student_blueprint = Blueprint('student_blueprint', __name__, url_prefix='/student')

@student_blueprint.route('/', methods=["POST"])
def create():
    id = Service().create(json.loads(request.data))
    return jsonify({'created':id})

@student_blueprint.route('/', methods=["GET"])
def get():
    students = Service().get()
    return jsonify({"students":students})

@student_blueprint.route('/<int:id>', methods=["PUT"])
def update(id: int):
    Service().update(id, json.loads(request.data))
    return jsonify({"updated": "Ok"})

@student_blueprint.route('/<int:id>', methods=["DELETE"])
def delete(id: int):
    Service().delete(id)
    return jsonify({"deleted": "Ok"})