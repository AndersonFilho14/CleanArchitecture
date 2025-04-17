from .user_finder import UserFider
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():

    first_name = "ANaaaaaaaaaaa"

    repositorio = UsersRepositorySpy( )
    user_finder = UserFider(repositorio)

    finder = user_finder.find(first_name= first_name)

    assert repositorio.select_user_attributes["first_name"] == first_name
    assert finder["type"] == "Users"
    assert finder["count"] == len(finder["attributes"])
    assert finder["attributes"] != []
