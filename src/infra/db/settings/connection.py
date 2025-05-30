from typing import Self, Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from src.infra.db.settings.base import Base


class DBConnectionHandler:
    """Classe de conexão com o banco
    """
    def __init__(self)->None:
        """asd

        """
        self.__connection_string = "sqlite:///users.db"
        self.__engine: Engine = self.__create_database_engine()
        Base.metadata.create_all(self.__engine)
        self.session: Optional[Session] = None

    def __create_database_engine(self)-> Engine:
        """Cria engine
        :return Engine: Engine
        """
        engine: Engine = create_engine(self.__connection_string)
        return engine

    def get__engine(self) -> Engine:
        """
        Cria uma sessão e retorna o próprio objeto.

        :return MinhaClasse: Instância da própria classe com a sessão criada.
        """
        return self.__engine

    def __enter__(self) -> Self:
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
