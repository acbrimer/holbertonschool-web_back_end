#!/usr/bin/env python3
""" Module for flask app """
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
