# region Import Modules...

from src.connections.sql_connection import SQLServerConnection
from src.extract.sql_extractor import get_max_id
from src.config.setting import *
import pandas as pd

# endregion

# region Server Config...

# ------------------------------- Source -------------------------------
source_server = SQLServerConnection(
    host=SOURCE_FISHES_HOST,
    port=1433,
    user=SOURCE_FISHES_USERNAME,
    password=SOURCE_FISHES_PASSWORD,
    database=SOURCE_FISHES_DATABASE,
    windows_auth=True
)
source_server.get_connection()

# ------------------------------- Source -------------------------------
target_server = SQLServerConnection(
    host=TARGET_FISHES_HOST,
    port=1433,
    user=TARGET_FISHES_USERNAME,
    password=TARGET_FISHES_PASSWORD,
    database=TARGET_FISHES_DATABASE,
    windows_auth=True
)
target_server.get_connection()

# endregion

# region Get MaxID...

max_id = get_max_id(source_server.engine, SOURCE_FISHES_SCHEMA, SOURCE_FISHES_TABLE, SOURCE_FISHES_PK)

# endregion
