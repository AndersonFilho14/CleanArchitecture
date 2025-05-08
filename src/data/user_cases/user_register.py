from src.errors.types import HttpBadRequestError
from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.domain.user_cases.user_register import UserRegister as UserRegisterInterface

class UserRegistrer(UserRegisterInterface):
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def registrar(self, first_name: str, last_name: str, age:int)-> dict:
        self.__validar_nome(first_name= first_name, last_name= last_name)
        self.__registry_user_information(first_name= first_name, last_name= last_name, age= age)
        response = self.__format_response(first_name=first_name, last_name= last_name, age= age)
        return response

    @classmethod
    def __validar_nome(cls, first_name:str, last_name:str) -> None:

        if not first_name.isalpha():
            raise HttpBadRequestError("Nome invalido para o cadastro")

        if len(first_name) > 21:
            raise HttpBadRequestError("Nome muito grande")

    def __registry_user_information(self, first_name:str, last_name: str, age: int) -> None:
        self.__user_repository.insert_user(first_name= first_name, last_name= last_name, age= age)

    @classmethod
    def __format_response(cls, first_name:str, last_name:str, age: int)->dict:
        response = {
            "type": "Users",
            "count": 1,
            "attibutes": {
                "first_name": first_name,
                "last_name": last_name ,
                "age": age

            }
        }
        return response
