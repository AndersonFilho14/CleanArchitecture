from src.domain.models.users import Users
from src.infra.db.entites.user import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.interfaces.users_repositories import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name:str, last_name: str, age:int ) -> None:
        with DBConnectionHandler() as database:
            assert database.session is not None
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


    @classmethod
    def select_user(cls, first_name: str) -> list[Users]:
        with DBConnectionHandler() as database:
            assert database.session is not None
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
