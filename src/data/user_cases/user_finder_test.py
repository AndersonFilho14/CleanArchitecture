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

def test_find_error_validar_nome():

    first_name = "Ana123"
    repositorio = UsersRepositorySpy( )
    user_finder = UserFider(repositorio)

    try:
        user_finder.find(first_name= first_name)
        assert False
    except Exception as e:
        assert str(e) == "Nome invalido para o find"

def test_find_error_long():

    first_name = "Anaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    repositorio = UsersRepositorySpy( )
    user_finder = UserFider(repositorio)

    try:
        user_finder.find(first_name= first_name)
        assert False
    except Exception as e:
        assert str(e) == "Nome muito grande"

def test_find_error_nao_ter_user ():

    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name):
            return []

    first_name = "Ana"
    repositorio = UsersRepositoryError( )
    user_finder = UserFider(repositorio)

    try:
        user_finder.find(first_name= first_name)
        assert False
    except Exception as e:
        assert str(e) == "User não encontrado"
