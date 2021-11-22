#!/usr/bin/env python3
""" Module for auth """
from flask import request
from typing import List, TypeVar


def clean_url(url: str) -> str:
    """ clean_url - helper func for slash tolerant url match """
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
        if not path or not excluded_paths:
            return True
        return clean_url(path) not in [clean_url(p) for p in excluded_paths]

    def authorization_header(self, request=None) -> str:
        """ authorization_header
            If req is None, returns None
            If req doesn’t contain the header key Authorization, returns None
            Else, return the value of the header req Authorization
        """
        if not request:
            return None
        if 'Authorization' not in request.headers.keys():
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user - hardcoded None """
        print('Auth.current_user')
        return None
