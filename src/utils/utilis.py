# region modules...
import re

from sqlalchemy import text
from pathlib import Path

# endregion

# region Variables...

BASE_DIR = Path(__file__).parent.parent.parent
CREATE_SCHEMA = BASE_DIR / "sql" / "ddl" / "create_schema.sql"
CREATE_TABLE = BASE_DIR / "sql" / "ddl" / "create_table.sql"
EXTRACT_FULL = BASE_DIR / "sql" / "queries" / "extract_full.sql"
EXTRACT_MAX_ID = BASE_DIR / "sql" / "queries" / "extract_max_id.sql"
EXTRACT_COUNT = BASE_DIR / "sql" / "queries" / "extract_count.sql"


# endregion


# region Functions...

def create_schema(schema: str) -> str:
    """
    Creates the schema SQL file.
    :param path:
    :param schema:
    :return: create schema SQL query
    """
    global CREATE_SCHEMA
    with open(CREATE_SCHEMA, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        return text(query)


def create_table(schema: str, table: str) -> str:
    """
    Creates the table SQL file.
    :param path:
    :param schema:
    :return: create schema SQL query
    """
    global CREATE_TABLE
    with open(CREATE_TABLE, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        return text(query)


def extract_full(schema: str, table: str) -> str:
    """
    Extracts the full table SQL query.
    :param path:
    :param schema:
    :return: select SQL query
    """
    with open(EXTRACT_FULL, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        return text(query)


def extract_max_id(schema: str, table: str, column: str) -> str:
    """
    EXTRACT_MAX_ID SQL query.
    :param path:
    :param schema:
    :param table:
    :return: max id SQL query
    """
    with open(EXTRACT_MAX_ID, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        query = query.replace("id", column)
        return text(query)


def extract_count(schema: str, table: str) -> str:
    """
    EXTRACT_COUNT SQL query.
    :param path:
    :param schema:
    :param table:
    :return: count(*) SQL query
    """
    with open(EXTRACT_COUNT, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        return text(query)

# endregion
