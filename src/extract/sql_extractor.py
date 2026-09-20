from src.connections.sql_connection import SQLServerConnection
from src.config.setting import *
from src.utils import * 

# ------------------------------------ Configure SQLServer Connections ------------------------------------
source_server = SQLServerConnection(host=SOURCE_FISHES_HOST,
                                   port=1433,
                                   user=SOURCE_FISHES_USERNAME,
                                   password=SOURCE_FISHES_PASSWORD,
                                   database=SOURCE_FISHES_DATABASE,
                                   windows_auth=True)

target_server = SQLServerConnection(host=TARGET_FISHES_HOST,
                                   port=1433,
                                   user=TARGET_FISHES_USERNAME,
                                   password=TARGET_FISHES_PASSWORD,
                                   database=TARGET_FISHES_DATABASE,
                                   windows_auth=True)

def extract_query(query):
