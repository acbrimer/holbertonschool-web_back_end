#!/usr/bin/env python3
""" Module for basic_auth """
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """ BasicAuth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return None
        if ' ' not in authorization_header:
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header """
        try:
            b = base64.b64decode(base64_authorization_header)
            return b.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ extract_user_credentials """
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return decoded_base64_authorization_header.split(':')

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ user_object_from_credentials """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        users = User.search({"email": user_email})
        if not users:
            return None
        if not users[0].is_valid_password(user_pwd):
            return None
        return users[0]
