from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.domain.models.user_cases.user_finder import UserFinder as UserFinderInterface

class UserFider(UserFinderInterface):
    def __init__(self, users_repositories: UsersRepositoryInterface) -> None:
        self.users_repositories = users_repositories

    def  find(self, first_name:str)->dict: pass
