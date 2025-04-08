from sqlalchemy import create_engine, Engine

class DBConnectionHandler:
    """Classe de conexão com o banco
    """
    def __init__(self)->None:
        """asd

        """
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            '1234',
            'localhost',
            '3306',
            'clean_database'
        )
        self.__engine: Engine = self.__create_database_engine()

    def __create_database_engine(self)-> Engine:
        """Cria engine
        :return Engine: Engine
        """
        engine: Engine = create_engine(self.__connection_string)
        return engine

    def get__engine(self)-> Engine:
        """Retorna a engine

        :return Engine: Engine da conexão com o banco
        """
        return self.__engine
