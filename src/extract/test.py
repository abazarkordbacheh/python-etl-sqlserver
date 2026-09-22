from src.config.setting import *
from src.connections.sql_connection import SQLServerConnection
from src.extract.sql_extractor import extract,extract_where_max_id
import pandas as pd

from src.utils.utilis import extract_where


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


if __name__ == "__main__":
    conn = db()
    conn.get_connection()
    for df in  extract_where_max_id(conn.engine,"LTS", "fishes","fish_id","200"):
        df = pd.DataFrame(df)
        print(df)
