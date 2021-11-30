#!/usr/bin/env python3
""" Module for auth """
from sqlalchemy.orm import session
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid

salt = bcrypt.gensalt()


def _hash_password(password: str) -> bytes:
    """ Hashes password with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _generate_uuid(self) -> str:
        """ Gens a new uuid """
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound as e:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if email/pass combination is a valid login """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                    password.encode('utf8'), user.hashed_password)
            return False
        except NoResultFound as e:
            return False

    def create_session(self, email: str) -> str:
        """ Creates a session ID for user email """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                sesssionId = self._generate_uuid()
                self._db.update_user(user.id, session_id=sesssionId)
                return sesssionId
        except NoResultFound as e:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Gets user from session ID """
        if not session_id or not isinstance(session_id, str):
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
            return None
        except NoResultFound as e:
            return None

    def destroy_session(self, user_id: int):
        """ Updates users session_Id to none """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except Exception as e:
            return None

    def get_reset_password_token(self, email: str):
        """ Creates a reset token for user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                resetToken = self._generate_uuid()
                self._db.update_user(user.id, reset_token=resetToken)
                return resetToken
        except NoResultFound as e:
            return None

    def update_password(self, reset_token: str, password: str):
        """ Resets the password for a valid reset_token """
        if not reset_token or not password:
            raise ValueError()
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                pw = _hash_password(password)
                self._db.update_user(
                    user.id, password=pw, reset_token=None)
                return None
            else:
                raise ValueError()
        except Exception as e:
            raise ValueError()
