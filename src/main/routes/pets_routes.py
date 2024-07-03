from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

pet_route_bp = Blueprint('pets_routes', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def list_pets():
    request = HttpRequest()
    view = pet_lister_composer()

    response = view.handle(request)

    return jsonify(response.body), response.status_code

@pet_route_bp.route('/pets/<string:name>', methods=['DELETE'])
def delete_pet(name):
    request = HttpRequest(params={"name": name})
    view = pet_deleter_composer()

    response = view.handle(request)
    return jsonify(response.body), response.status_code
