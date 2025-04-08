import pytest
from .connection import  DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handler = DBConnectionHandler()

    engine = db_connection_handler.get__engine()

    assert engine is not None
