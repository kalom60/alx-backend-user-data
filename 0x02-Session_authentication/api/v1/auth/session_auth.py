#!/usr/bin/env python3
"""Session authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """creates SessionAuth calss"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        uid = str(uuid4())
        self.user_id_by_session_id[uid] = user_id
        return uid
