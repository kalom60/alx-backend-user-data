#!/usr/bin/env python3
"""script that creates Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """retrun bool based on the path"""
        return False

    def authorization_header(self, request=None) -> str:
        """method that authorize header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method return None"""
        return None
