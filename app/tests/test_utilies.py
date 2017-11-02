""" This module tests all functions in the utilites.py file """
import unittest
from app.utilities import register, login
from app.models import User
from app import USERS


class TestUTilityFunctions(unittest.TestCase):
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

    def test_none_inpts(self):
        """ Tests the register utilites functions against various inputs """
        self.assertEqual(register(None, None, None, None), "None input")

    def test_blank_credentials(self):
        """Ensure that credentials are not blank"""
        self.assertEqual(register("  ", " ", "  ", " "), "Blank input")

    def test_username_length_4_10(self):
        """Ensure that password characters are btn 4 and 10 """
        self.assertEqual(register(self.name, self.short_username,
                                  self.correct_password, self.correct_password),
                         "Username should be 4 to 10 characters")
        self.assertEqual(register(self.name, self.long_username, self.correct_password,
                                  self.correct_password),
                         "Username should be 4 to 10 characters")

    def test_password_length_6_10(self):
        """Ensure that password characters are btn 6 and 10 """
        
        self.assertEqual(register(self.name, self.correct_username, self.short_pass,
                                  self.short_pass),
                         "Password should be 6 to 10 characters")
        self.assertEqual(register(self.name, self.correct_username, self.long_pass,
                                  self.long_pass),
                         "Password should be 6 to 10 characters")

    def test_llegal_username_characters(self):
        """Ensure that illegal characters in username are not allowed"""

        self.assertEqual(register(self.name, self.invalid_chars_username, self.correct_password,
                                  self.correct_password),
                         "Illegal characters in username")

    def test_passwords_donot_match(self):
        """Ensure that passwords mismatch is not allowed"""
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.long_pass),
                         "Passwords don't match")

    def test_registration_successful(self):
        """Ensure registration is succesful"""
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.correct_password),
                         "Registration successful")


    def test_login_none(self):
        """ Tests the login method of the views module for None in put """
        self.assertEqual(login(None, None), "None input")

    def test_login_blank(self):
        """ Tests the login method of the views module for blank input """
        self.assertEqual(login(" ", " "), "Blank input")

    def test_login_unknown(self):
        """ Tests the login method of the views module for unknown user """
        self.assertEqual(login("unknownuser", "unknownpass"), "User not found")
        USERS[self.correct_username] = User(self.name, self.correct_username,
                                            self.correct_password)

    def test_login_wrongpass(self):
        """ Tests the login method of the views module for wrong password """
        self.assertEqual(login(self.correct_username, "wrongpass"), "Wrong password")

    def test_login_success(self):
        """ Tests the login method of the views module for Ncorrect password """
        register(self.name, self.correct_username, self.correct_password,
                 self.correct_password)
        self.assertEqual(login(self.correct_username, self.correct_password), "Login successful")                     


if __name__ == '__main__':
    unittest.main()
