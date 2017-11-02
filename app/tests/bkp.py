""" This module tests all functions in the utilites.py file """
import unittest
from app.utilities import register


class TestUTilityFunctions(unittest.TestCase): 
    """ This class tests methods of the views module """
    def setUp(self):
        self.name = "Eric Elem"
        self.correct_username = "eric.elem"
        self.short_username = "eri"
        self.long_username = "ericnelsonelem"
        self.invalid_chars_username = "eric@elem"
        self.correct_password = "password"
        self.short_pass = "pass"
        self.long_pass = "passwordpassword"

    def test_utilities(self):
        """ Tests the register utilites functions against various inputs """
        self.assertEqual(register(None, None, None, None), "None input")
        """Ensure that credentials are not blank"""

    def test_blank_credentials(self):
        """Ensure that user name is between 4 and 10 characters"""
        self.assertEqual(register("  ", " ", "  ", " "), "Blank input")

    def test_username_length_4_10(self):
        """Enure that password characters are btn 6 and 10 """
        self.assertEqual(register(self.name, self.short_username,
                                  self.correct_password, self.correct_password),
                         "Username should be 4 to 10 characters")
        self.assertEqual(register(self.name, self.long_username, self.correct_password,
                                  self.correct_password),
                         "Username should be 4 to 10 characters")

    def test_password_length_6_10(self):
        """Ensure that all username characters are illegal is not allowed"""
        self.assertEqual(register(self.name, self.correct_username, self.short_pass,
                                  self.short_pass),
                         "Password should be 6 to 10 characters")
        self.assertEqual(register(self.name, self.correct_username, self.long_pass,
                                  self.long_pass),
                         "Password should be 6 to 10 characters")

    def test_illegal_username_characters(self):
        """Ensure that illegal characters are not allowed"""

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








if __name__ == '__main__':
    unittest.main()
