#!/usr/bin/env python3
"""authorization module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """function that hash a string password"""
    ency = password.encode('UTF-8')
    return bcrypt.hashpw(ency, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method to register a new user"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user
        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """method to validate a user by its email and password"""
        try:
            user = self._db.find_user_by(email=email)
            ency = password.encode('utf-8')
            if bcrypt.checkpw(ency, user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False
