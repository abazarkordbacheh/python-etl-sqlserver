from src.connections.base import ConnectionBase
import sqlalchemy
import pymssql


class SQLServerConnection(ConnectionBase):
    """
    Connected to SQL Server by sqlalchemy
    :Args:
    host: Server Ip address
    Port: Server Port
    User: Username
    Password: Password
    Database: Database
    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str,
                 windows_auth: bool = True) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.windows_auth = windows_auth

    def get_connection(self):
        """
        Get connection to SQL Server
        :return:
        sqlalchemy.engine.base.Engine
        """

        if self.windows_auth:
            conn_str = f"mssql+pymssql://{self.host}:{self.port}/{self.database}"
            self.engine = sqlalchemy.create_engine(conn_str)
        else:
            conn_str = (
                f"mssql+pymssql://{self.user}:{self.password}"
                f"@{self.host}:{self.port}/{self.database}"
            )
            self.engine = sqlalchemy.create_engine(conn_str)

    @classmethod
    def sample(cls) -> SQLServerConnection:
        return SQLServerConnection(host="localhost",
                                   port=1433,
                                   user="",
                                   password="",
                                   database="master",
                                   windows_auth=True)
