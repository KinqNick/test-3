import unittest
from src.database import connection

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.connection = connection.DatabaseConnection()

    def test_connection(self):
        self.assertIsNotNone(self.connection.connect())

    def test_invalid_credentials(self):
        with self.assertRaises(connection.DatabaseConnectionError):
            connection.DatabaseConnection('invalid_user', 'invalid_password')

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()