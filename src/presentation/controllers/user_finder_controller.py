from src.presentation.interfaces.crontroller_interface import ControllerInterface
from src.domain.user_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserFinderController(ControllerInterface):
    def __init__(self, user_case: UserFinderInterface) -> None:
        self.__user_case = user_case

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        username = http_request.query_params["first_name"]

        retorno = self.__user_case.find(first_name= username)

        return HttpResponse(status_code= 200, body={"data": retorno})
