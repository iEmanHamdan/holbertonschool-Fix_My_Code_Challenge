#!/usr/bin/python3
"""
User class implementation
"""


class User:
    """User class with password validation"""

    def __init__(self, email=None, password=None):
        """Initialize user email and password"""
        self.email = email
        self.password = password

    def is_valid_password(self, password):
        """Validate password"""
        if password is None:
            return False
        if self.password is None:
            return False
        return self.password == password
