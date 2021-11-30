#!/usr/bin/env python3
""" Module for flask app """
from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
