import unittest
from src.controllers.user_controller import get, post, update, delete

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_data = {
            "name": "Test User",
            "email": "testuser@example.com"
        }

    def test_get(self):
        response = get(self.user_id)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = post(self.user_data)
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        response = update(self.user_id, self.user_data)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = delete(self.user_id)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()