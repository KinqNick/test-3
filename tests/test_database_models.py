import unittest
from src.database import models

class TestDatabaseModels(unittest.TestCase):

    def setUp(self):
        self.user_model = models.User()
        self.product_model = models.Product()

    def test_user_model(self):
        self.assertIsNotNone(self.user_model)
        self.assertTrue(hasattr(self.user_model, 'get'))
        self.assertTrue(hasattr(self.user_model, 'post'))
        self.assertTrue(hasattr(self.user_model, 'update'))
        self.assertTrue(hasattr(self.user_model, 'delete'))

    def test_product_model(self):
        self.assertIsNotNone(self.product_model)
        self.assertTrue(hasattr(self.product_model, 'get'))
        self.assertTrue(hasattr(self.product_model, 'post'))
        self.assertTrue(hasattr(self.product_model, 'update'))
        self.assertTrue(hasattr(self.product_model, 'delete'))

if __name__ == '__main__':
    unittest.main()