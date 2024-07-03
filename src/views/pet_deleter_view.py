from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.params['name']
        self.__controller.delete(name)

        return HttpResponse(status_code=204)
