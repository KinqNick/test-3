import unittest
from src.main import main
from src.utils import log_error, validate_data

class TestMain(unittest.TestCase):

    def setUp(self):
        self.main = main

    def test_main(self):
        self.assertEqual(self.main(), "Main function executed successfully")

    def test_log_error(self):
        self.assertEqual(log_error("Test Error"), "ERROR: Test Error")

    def test_validate_data(self):
        self.assertTrue(validate_data({"name": "Test", "email": "test@test.com"}))
        self.assertFalse(validate_data({"name": "", "email": "test@test.com"}))

if __name__ == '__main__':
    unittest.main()