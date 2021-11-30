#!/usr/bin/env python3
""" Module for auth """
import bcrypt

salt = bcrypt.gensalt()


def _hash_password(password: str) -> bytes:
    """ Hashes password with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf8'), salt)
