from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entites.user import Users as UsersEntity


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name:str, last_name: str, age:int ) -> None:
        with DBConnectionHandler() as database:
            try:
                registro_novo = UsersEntity(
                    first_name= first_name,
                    last_name= last_name,
                    age = age
                )
                database.session.add(registro_novo)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
