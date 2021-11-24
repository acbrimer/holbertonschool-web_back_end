#!/usr/bin/env python3
""" Module for session_auth view """
from api.v1.views import app_views
from models.user import User
from flask import abort, jsonify, request
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ loging - function to handle login requests """
    email = request.form.get('email', None)
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password', None)
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(users[0].id)
        out = jsonify(users[0].to_json())
        cookie_name = os.environ.get('SESSION_NAME')
        out.set_cookie(cookie_name, session_id)
        return out


@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ logout - calls function to remove session """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify(dict({})), 200
    abort(404)
