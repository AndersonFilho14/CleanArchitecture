from src.data.user_cases.user_finder import UserFider
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.controllers.user_finder_controller import  UserFinderController


def user_finder_composer():
    repositorio = UsersRepository()
    caso_de_uso = UserFider(repositorio)
    controller = UserFinderController(caso_de_uso)

    return controller.handle