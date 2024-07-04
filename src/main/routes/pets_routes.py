from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

from src.errors.error_handler import handle_errors

pet_route_bp = Blueprint('pets_routes', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def list_pets():
    try:
        request = HttpRequest()
        view = pet_lister_composer()

        response = view.handle(request)
        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response.body), response.status_code

@pet_route_bp.route('/pets/<string:name>', methods=['DELETE'])
def delete_pet(name):
    try:
        request = HttpRequest(params={"name": name})
        view = pet_deleter_composer()

        response = view.handle(request)
        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response.body), response.status_code
