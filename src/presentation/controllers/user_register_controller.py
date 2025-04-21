from src.presentation.interfaces.crontroller_interface import ControllerInterface
from src.domain.user_cases.user_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserRegisterController(ControllerInterface):
    def __init__(self, user_case: UserRegisterInterface) -> None:
        self.__user_case = user_case

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        username = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]

        retorno = self.__user_case.registrar(first_name= username, last_name= last_name, age= age)

        return HttpResponse(status_code= 200, body={"data": retorno})
