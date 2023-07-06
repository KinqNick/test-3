import unittest
from src.controllers.product_controller import get, post, update, delete

class TestProductController(unittest.TestCase):

    def setUp(self):
        self.product_id = 1
        self.product_data = {
            "name": "Test Product",
            "description": "This is a test product",
            "price": 100.0
        }

    def test_get(self):
        response = get(self.product_id)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = post(self.product_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], self.product_data['name'])

    def test_update(self):
        updated_data = self.product_data.copy()
        updated_data['price'] = 150.0
        response = update(self.product_id, updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['price'], updated_data['price'])

    def test_delete(self):
        response = delete(self.product_id)
        self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()