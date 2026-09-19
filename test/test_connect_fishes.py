from src.config.setting import *
from src.connections.sql_connection import SQLServerConnection
import pytest


@pytest.fixture
def db():
    conn = SQLServerConnection(
        host=SOURCE_FISHES_HOST,
        port=1433,
        user=SOURCE_FISHES_USERNAME,
        password=SOURCE_FISHES_PASSWORD,
        database=SOURCE_FISHES_DATABASE,
        windows_auth=True
    )
    return conn


def test_connection_returns_engine(db):
    engine = db.get_connection()
    assert engine is not None


def test_can_execute_query(db):
    engine = db.get_connection()
    with engine.connect() as con:
        result = con.execute("SELECT 1 AS val")
        row = result.fetchone()
        assert row["val"] == 1
