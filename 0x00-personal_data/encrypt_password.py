#!/usr/bin/env python3
"""script that encripts passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that hash a password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
