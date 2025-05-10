from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_finder_validator(request: any):
    query_validador = Validator({
        "first_name": { "type": "string", "required": True, "empty": False}
    })

    response = query_validador.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validador.errors)
