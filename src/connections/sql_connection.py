from base import ConnectionBase
import sqlalchemy


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

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        """
        Get connection to SQL Server
        :return:
        sqlalchemy.engine.base.Engine
        """
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )
        return engine
