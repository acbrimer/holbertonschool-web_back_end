#!/usr/bin/env python3
""" Module for session_auth """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth """
    user_id_by_session_id = dict({})

    def create_session(self, user_id: str = None) -> str:
        """ create_session - creates a Session ID for user_id """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
