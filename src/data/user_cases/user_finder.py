from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.domain.models.user_cases.user_finder import UserFinder as UserFinderInterface

class UserFider(UserFinderInterface):
    def __init__(self, users_repositories: UsersRepositoryInterface) -> None:
        self.__users_repositories = users_repositories

    def  find(self, first_name:str)->dict:

        if not first_name.isalpha():
            raise Exception("Nome invalido para o find")

        if len(first_name) > 21:
            raise Exception("Nome muito grande")

        users = self.__users_repositories.select_user(first_name= first_name)
        if users == []:
            raise Exception("User não encontrado")

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response
