#!/usr/bin/env python3
""" Module for auth """
from flask import request
from typing import List, TypeVar


def clean_url(url: str) -> str:
    return url[:-1] if url[-1] == '/' else url


class Auth:
    """ Auth class
        Handles authentication to API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
            Returns True if path is None
            Returns True if excluded_paths is None or empty
            Returns False if path is in excluded_paths
        """
        return clean_url(path) in [clean_url(p) for p in excluded_paths]

    def authorization_header(self, request=None) -> str:
        """ authorization_header - hardcoded None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user - hardcoded None """
