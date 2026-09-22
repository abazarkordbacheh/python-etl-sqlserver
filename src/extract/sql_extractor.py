from typing import Any
from src.connections.sql_connection import SQLServerConnection
from src.utils.utilis import extract_full
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