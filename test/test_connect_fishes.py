import sqlalchemy

from src.config.setting import *
from src.connections.sql_connection import SQLServerConnection
import pytest


@pytest.fixture
def db() -> SQLServerConnection:
    """
    Create a connection to SQL Server
    :return: SQLServerConnection
    """
    conn = SQLServerConnection(
        host=SOURCE_FISHES_HOST,
        port=1433,
        user=SOURCE_FISHES_USERNAME,
        password=SOURCE_FISHES_PASSWORD,
        database=SOURCE_FISHES_DATABASE,
        windows_auth=True
    )
    return conn


def test_connection_returns_engine(db: SQLServerConnection) -> None:
    """
    Test that the engine is returned
    :param db:
    :return: None
    """
    engine = db.get_connection()
    assert engine is not None


def test_can_execute_query(db) -> None:
    """
    Test that the engine is executed
    :param db:
    :return: None
    """
    engine = db.get_connection()
    with engine.connect() as con:
        result = con.execute(sqlalchemy.text("SELECT 1 AS val"))
        row = result.fetchone()
        assert row.val == 1
        assert row[0] == 1
        assert row._mapping["val"]
