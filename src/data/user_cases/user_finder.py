from src.domain.models.users import Users
from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.domain.user_cases.user_finder import UserFinder as UserFinderInterface

class UserFider(UserFinderInterface):
    def __init__(self, users_repositories: UsersRepositoryInterface) -> None:
        self.__users_repositories = users_repositories

    def  find(self, first_name:str)->dict:

        self.__validar_nome(first_name= first_name)
        users: list[Users] = self.__search_user(first_name= first_name)
        response = self.__formarta_response(users= users)
        return response

    @classmethod
    def __validar_nome(cls, first_name:str) -> None:

        if not first_name.isalpha():
            raise Exception("Nome invalido para o find")

        if len(first_name) > 21:
            raise Exception("Nome muito grande")

    def __search_user(self, first_name:str) -> list:
        users = self.__users_repositories.select_user(first_name= first_name)
        if users == []:
            raise Exception("User não encontrado")
        return users

    @classmethod
    def __formarta_response(cls, users: list[Users]):
        atrributes  = []
        for user in users:
            atrributes.append(
                {"first_name": user.first_name,
                 "last_name": user.last_name,
                 "age" : user.age}
            )
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": atrributes
        }
        return response
