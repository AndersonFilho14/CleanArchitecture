import pytest
from sqlalchemy import text
from .users_repository import UsersRepository
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get__engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_user() -> None:
    mocked_first_name = 'ande'
    mocked_last_name = 'muito'
    mocked_age = 214

    user_repositories = UsersRepository()
    user_repositories.insert_user(first_name= mocked_first_name, last_name= mocked_last_name, age= mocked_age)

    sql = '''
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = '{}'
        '''.format(mocked_first_name, mocked_last_name, mocked_age)
    response = connection.execute(text(sql))
    registro = response.fetchall()[0]

    assert registro.first_name == mocked_first_name
    assert registro.last_name == mocked_last_name
    assert registro.age == mocked_age

    connection.execute(text(f"""
            DELETE FROM users WHERE id = {registro.id}
                       """))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user() -> None:
    mocked_first_name = 'first_2'
    mocked_last_name = 'last_2'
    mocked_age = 51

    sql = '''
        INSERT INTO users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
    '''.format(mocked_first_name, mocked_last_name, mocked_age)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_first_name)
    print(f"response  {response}")

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))
    connection.commit()
