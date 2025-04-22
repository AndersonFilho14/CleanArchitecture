from src.data.tests.user_finder import UserFinderSpy
from src.presentation.controllers.user_finder_controller import UserFinderController
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock():
    def __init__(self):
        self.query_params = {"first_name": "teste"}

def test_handler():
    http_request_mockando = HttpRequestMock()
    user_case = UserFinderSpy()
    user_finder_controller = UserFinderController(user_case=user_case)

    retorno = user_finder_controller.handle(http_request= http_request_mockando)

    assert isinstance(retorno, HttpResponse)
    assert retorno.status_code == 200
    assert retorno.body["data"] is not None
#testando code sp
