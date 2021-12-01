#!/usr/bin/env python3
""" Module for flask app """
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ Base URL for flask app """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email', None)
    pw = request.form.get('password', None)
    if not email or not pw or not AUTH.valid_login(email, pw):
        abort(401)
    sessionId = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", sessionId)
    return res


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Finds user by session_id cookie and logs out if exists """
    sessionId = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sessionId)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/", 302)
    abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ Returns JSON for user tied to session_id cookie """
    sessionId = request.cookies.get('session_id', None)
    if not sessionId:
        abort(403)
    user = AUTH.get_user_from_session_id(sessionId)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_password():
    """ Creates a reset token for user email """
    email = request.form.get('email', None)
    if not email:
        abort(403)
    token = AUTH.get_reset_password_token(email)
    if not token:
        abort(403)
    return jsonify({"email": email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ Update the users password using reset_token """
    email = request.form.get('email', None)
    resetToken = request.form.get('reset_token', None)
    pw = request.form.get('new_password', None)
    try:
        AUTH.update_password(resetToken, pw)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError as e:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
