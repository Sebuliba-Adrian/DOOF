import unittest
from app.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Adrian", "adris", "secret")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    
    def test_add_category_None(self):
         self.assertEqual(self.user.add_category(None), "None input")

    def test_add_category_blank_input(self):
        self.assertEqual(self.user.add_category(" "), "Blank input")
