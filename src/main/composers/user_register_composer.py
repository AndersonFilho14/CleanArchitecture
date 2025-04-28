from src.data.user_cases.user_register import UserRegistrer
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.controllers.user_register_controller import UserRegisterController


def user_register_composer():
    repositorio = UsersRepository()
    caso_de_uso = UserRegistrer(repositorio)
    controller = UserRegisterController(caso_de_uso)

    return controller.handle

    