#!/usr/bin/env python3
""" Module for auth """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
        Handles authentication to API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth - hardcoded to return False """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header - hardcoded None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user - hardcoded None """
