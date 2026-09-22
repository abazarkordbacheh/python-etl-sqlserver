from typing import Any
from src.connections.sql_connection import SQLServerConnection
from src.utils.utilis import extract_full, extract_max_id, extract_where
import pandas as pd


# ------------------------------------ Configure SQLServer Connections ------------------------------------
def extract(connection: SQLServerConnection, schema: str, table: str) -> Any:
    """
    Extract data from SQL table
    :param connection:
    :param schema:
    :param table:
    :return: Generator
    """
    query = extract_full(schema, table)
    with connection.engine.connect() as conn:
        for chunk in pd.read_sql_query(query, con=conn, chunksize=10):
            yield chunk


def get_max_id(connection: SQLServerConnection, schema: str, table: str, column: str) -> str:
    """
    Get max id from SQL table
    :param connection:
    :param schema:
    :param table:
    :return: str(int(max id))
    """
    query = extract_max_id(schema, table, column)
    with connection.engine.connect() as conn:
        max_id = str(conn.execute(query).fetchone()[0])
        return max_id

def extract_where_max_id(connection: SQLServerConnection,schema: str, table: str, column: str, max_id:str) -> Any:
    query = extract_where(schema, table,column,max_id)
    with connection.engine.connect() as conn:
        for chunk in pd.read_sql_query(query, con=conn, chunksize=10):
            yield chunk