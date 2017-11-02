""" This module contains all the helper functions for the recipes app"""
import re
from app import USERS
from models import User


def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if name.strip() and username.strip() and password.strip() and rpt_password.strip():
            if len(username) > 3 and len(username) < 11:
                if re.match("^[a-zA-Z0-9_.-]+$", username):
                    if len(password) > 5 and len(password) < 11:
                        if password == rpt_password:
                            USERS[username] = User(name, username, password)
                            return "Registration successful"
                        return "Passwords don't match"
                    return "Password should be 6 to 10 characters"
                return "Illegal characters in username"
            return "Username should be 4 to 10 characters"
        return "Blank input"
    return "None input"


def login(username, password):
    """ Handles user login """
    if username and password:
        if username.strip() and password.strip():
            if USERS.get(username):
                if USERS[username].password == password:
                    return "Login successful"
                return "Wrong password"
            return "User not found"
        return "Blank input"
    return "None input"
