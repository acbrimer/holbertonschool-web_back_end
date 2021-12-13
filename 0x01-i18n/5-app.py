#!/usr/bin/env python3
""" Module for 0-app """
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns user dict or None from login_as request arg"""
    user_id = request.args.get('login_as', None)
    if user_id:
        if int(user_id) in users.keys():
            return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """logic to run before any other on request"""
    g.user = get_user()


class Config(object):
    """Config class for flask_babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get_locale - determines best language match for request """
    if request.args.get('locale', None):
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ index - returns the index template """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
