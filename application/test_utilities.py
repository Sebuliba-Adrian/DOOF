""" This module tests all functions in the categorylist app """
import unittest
from utilities import register, login, users_store
from models import User
class TestViewMethods(unittest.TestCase):
    """ This class tests methods of the views module """
    def setUp(self):
        self.name = "Adri Morg"
        self.correct_username = "adri.morg"
        self.short_username = "adr"
        self.long_username = "adrianmorgangreg"
        self.invalid_chars_username = "adris@morg"
        self.correct_password = "password"
        self.short_pass = "pass"
        self.long_pass = "passwordpassword"

    def test_register(self):
        """ Tests the register method of the views class against various inputs """
        self.assertEqual(register(None, None, None, None), "None input")
        self.assertEqual(register("  ", " ", "  ", " "), "Blank input")
        self.assertEqual(register(self.name, self.short_username,
                                  self.correct_password, self.correct_password),
                         "Username should be 4 to 10 characters")
        self.assertEqual(register(self.name, self.long_username, self.correct_password,
                                  self.correct_password),
                         "Username should be 4 to 10 characters")
        self.assertEqual(register(self.name, self.correct_username, self.short_pass,
                                  self.short_pass),
                         "Password should be 6 to 10 characters")
        self.assertEqual(register(self.name, self.correct_username, self.long_pass,
                                  self.long_pass),
                         "Password should be 6 to 10 characters")
        self.assertEqual(register(self.name, self.invalid_chars_username, self.correct_password,
                                  self.correct_password),
                         "Illegal characters in username")
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.long_pass),
                         "Passwords don't match")
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.correct_password),
                         "Registration successful")

    def test_login(self):
        """ Tests the login method of the views module """
        self.assertEqual(login(None, None), "None input")
        self.assertEqual(login(" ", " "), "Blank input")
        self.assertEqual(login("unknownuser", "unknownpass"), "User not found")
        users_store[self.correct_username] = User(self.name, self.correct_username,
                                            self.correct_password)
        self.assertEqual(login(self.correct_username, "wrongpass"), "Wrong password")
        self.assertEqual(login(self.correct_username, self.correct_password), "Login successful")


                      
if __name__ == '__main__':
    unittest.main()
