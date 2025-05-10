from src.data.user_cases.user_register import UserRegistrer
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test():
    first_name:str = "Primeiro"
    last_name:str = "sobrenome"
    age:int = 2

    repositorio = UsersRepositorySpy()
    user_register = UserRegistrer(user_repository=repositorio)

    retorno:dict = user_register.registrar(first_name= first_name, last_name= last_name, age= age)

    assert retorno["type"] == "Users"
    assert retorno["attibutes"]["first_name"] == first_name
    assert retorno["attibutes"]["last_name"] == last_name
    assert retorno["attibutes"]["age"] == age

def test_register_name_error():
    first_name:str = "5 nome"
    last_name:str = "sobrenome"
    age:str = 1

    repositorio = UsersRepositorySpy()
    user_register = UserRegistrer(user_repository=repositorio)

    try:
        user_register.registrar(first_name= first_name, last_name= last_name , age= age)
        assert False
    except Exception as e:
        assert str(e) == "Nome invalido para o cadastro"
