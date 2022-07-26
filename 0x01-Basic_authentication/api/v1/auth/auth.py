#!/usr/bin/env python3
"""script that creates Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """retrun bool based on the path"""
        if path:
            if path[-1] == '/':
                path = path[:-1]
        if excluded_paths:
            for i in range(len(excluded_paths)):
                if excluded_paths[i][-1] == '/':
                    excluded_paths[i] = excluded_paths[i][:-1]
        if excluded_paths is None or path is None or\
                len(excluded_paths) == 0 or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """method that authorize header"""
        if 'Authorization' in request.headers:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method return None"""
        return None
