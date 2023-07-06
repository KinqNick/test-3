import unittest
from src.views.user_view import UserView

class TestUserView(unittest.TestCase):

    def setUp(self):
        self.user_view = UserView()

    def test_user_list(self):
        user_list = self.user_view.get_user_list()
        self.assertIsNotNone(user_list, "ERROR_INVALID_DATA")

    def test_user_detail(self):
        user_detail = self.user_view.get_user_detail(1)
        self.assertIsNotNone(user_detail, "ERROR_INVALID_DATA")

if __name__ == '__main__':
    unittest.main()