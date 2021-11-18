#!/usr/bin/env python3
""" Module for encrypt_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash_password - hashes a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ is_valid - checks if password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
