import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_error_handling(self):
        self.assertEqual(utils.error_handling(400), "ERROR_INVALID_DATA")
        self.assertEqual(utils.error_handling(500), "ERROR_DATABASE_CONNECTION")

    def test_data_validation(self):
        self.assertTrue(utils.data_validation({"name": "test", "email": "test@test.com"}))
        self.assertFalse(utils.data_validation({"name": "", "email": "test@test.com"}))

    def test_logging(self):
        self.assertTrue(utils.logging("SUCCESS_POST"))
        self.assertTrue(utils.logging("SUCCESS_DELETE"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()