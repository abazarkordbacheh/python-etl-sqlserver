from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
CREATE_SCHEMA = BASE_DIR / "sql" / "ddl" / "create_schema.sql"
CREATE_TABLE = BASE_DIR / "sql" / "ddl" / "create_table.sql"


def create_schema(path: str, schema: str) -> str:
    with open(path, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        return query


def create_table(path: str, schema: str, table: str) -> str:
    with open(path, 'r') as f:
        query = f.read()
        query = query.replace("schema", schema)
        query = query.replace("table", table)
        return query

