import unittest

from src.connections.sql_connection import SQLServerConnection


class SQLServerConnectionTest(unittest.TestCase):
    """
    Check SQLServerConnection class attributes and methods
    """

    def setUp(self) -> None:
        self.connection = SQLServerConnection(host=".",
                                              port=1433,
                                              user="",
                                              password="",
                                              database="master",
                                              windows_auth=True).sample()

    def test_all_data(self) -> None:
        instance = self.connection
        instance.get_connection()

        self.assertIsInstance(instance, SQLServerConnection, "sample does not return instance of SQLServerConnection ")
        self.assertTrue(hasattr(instance, "get_connection"), "get_connection methods")


if __name__ == "__main__":
    unittest.main()
    print("All tests passed")
