#!/usr/bin/env python3
"""authorization module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """function that hash a string password"""
    ency = password.encode('UTF-8')
    return bcrypt.hashpw(ency, bcrypt.gensalt())
