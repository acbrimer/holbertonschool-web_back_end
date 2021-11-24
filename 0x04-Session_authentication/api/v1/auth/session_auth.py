#!/usr/bin/env python3
""" Module for session_auth """
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth """
    user_id_by_session_id = dict({})

    def create_session(self, user_id: str = None) -> str:
        """ create_session - creates a Session ID for user_id """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id_for_session_id - gets user_id for session_id """
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ current_user - overload to return User from cookie val """
        session_id_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ destroy_session - logout function to remove session """
        if request is None:
            return False
        session_id_cookie = self.session_cookie(request)
        if not session_id_cookie:
            return False
        user_id = self.user_id_for_session_id(session_id_cookie)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_id_cookie, None)
        return True
