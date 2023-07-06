import unittest
from src.views.product_view import ProductView

class TestProductView(unittest.TestCase):

    def setUp(self):
        self.product_view = ProductView()

    def test_product_list(self):
        product_list = self.product_view.get_product_list()
        self.assertIsNotNone(product_list, "ERROR_INVALID_DATA")

    def test_product_detail(self):
        product_detail = self.product_view.get_product_detail(1)
        self.assertIsNotNone(product_detail, "ERROR_INVALID_DATA")

    def test_update_product_detail(self):
        result = self.product_view.update_product_detail(1, {"name": "Updated Product"})
        self.assertEqual(result, "SUCCESS_POST")

    def test_delete_product(self):
        result = self.product_view.delete_product(1)
        self.assertEqual(result, "SUCCESS_DELETE")

if __name__ == "__main__":
    unittest.main()