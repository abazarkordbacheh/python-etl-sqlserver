import unittest
from src.connections.sql_connection import SQLServerConnection


class SQLServerConnectionTest(unittest.TestCase):
    """
    Check SQLServerConnection class attributes and methods
    """

    def setUp(self) -> None:
        """
        Set up the test case
        :return: None
        """
        self.instance = SQLServerConnection(host=".",
                                            port=1433,
                                            user="",
                                            password="",
                                            database="master",
                                            windows_auth=True).sample()

    def tearDown(self):
        """
        Clean up after each test
        :return: None
        """
        self.instance = None

    def test_all_data(self) -> None:
        """
        Check if all data is available
        :return: None
        """
        self.instance.get_connection()

        self.assertIsInstance(self.instance, SQLServerConnection,
                              "sample does not return instance of SQLServerConnection ")
        self.assertTrue(hasattr(self.instance, "get_connection"), "get_connection methods")

    def test_validation_params(self) -> None:
        """
        Check if all parameters are valid
        :return: None
        """
        self.assertIsInstance(self.instance.host, str, "host should be a string")
        self.assertIsInstance(self.instance.port, int, "port should be a int")
        self.assertIsInstance(self.instance.user, str, "user should be a string")
        self.assertIsInstance(self.instance.password, str, "password should be a string")
        self.assertIsInstance(self.instance.database, str, "database should be a string")
        self.assertIsInstance(self.instance.windows_auth, bool, "windows_auth should be a bool")


if __name__ == '__main__':
    unittest.main()
