#!/usr/bin/env python3
""" Module for auth """
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound

salt = bcrypt.gensalt()


def _hash_password(password: str) -> bytes:
    """ Hashes password with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound as e:
            return self._db.add_user(email, _hash_password(password))
