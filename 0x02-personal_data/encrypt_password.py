#!/usr/bin/env python3
""" Module for encrypt_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash_password - hashes a password """
    return bcrypt.hashpw(password, bcrypt.gensalt())
