from .users_repository import UsersRepository

def test_insert_user() -> None:
    mocked_first_name = 'first'
    mocked_last_name = 'second'
    mocked_age = 18

    user_repositories = UsersRepository()
    user_repositories.insert_user(first_name= mocked_first_name, last_name= mocked_last_name, age= mocked_age)
