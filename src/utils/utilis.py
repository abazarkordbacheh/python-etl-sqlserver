# region modules...
from __init__ import BASE_DIR

# endregion

# region Variables...

CREATE_SCHEMA = BASE_DIR / "sql" / "ddl" / "create_schema.sql"
CREATE_TABLE = BASE_DIR / "sql" / "ddl" / "create_table.sql"


# endregion


# region Functions...

def create_schema(path: str, schema: str) -> str:
    """
    Creates the schema SQL file.
    :param path:
    :param schema:
    :return: create schema SQL query
    """
    with open(path, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        return query


def create_table(path: str, schema: str, table: str) -> str:
    """
        Creates the table SQL file.
        :param path:
        :param schema:
        :return: create schema SQL query
        """
    with open(path, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        return query

# endregion
