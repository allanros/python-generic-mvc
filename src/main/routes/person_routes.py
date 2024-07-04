#pylint: disable=R0801
from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer

from src.errors.error_handler import handle_errors

person_route_bp = Blueprint('person_routes', __name__)

@person_route_bp.route('/people', methods=['POST'])
def list_pets():
    try:
        http_request = HttpRequest(body=request.json)
        view = person_creator_composer()

        response = view.handle(http_request)
        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response.body), response.status_code


@person_route_bp.route('/people/<int:person_id>', methods=['GET'])
def find_person(person_id):
    try:
        http_request = HttpRequest(params={'person_id': person_id})
        view = person_finder_composer()

        response = view.handle(http_request)
        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response.body), response.status_code
