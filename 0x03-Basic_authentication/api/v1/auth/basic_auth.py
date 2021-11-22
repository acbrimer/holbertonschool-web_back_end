#!/usr/bin/env python3
""" Module for basic_auth """
from api.v1.auth.auth import Auth


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
