#!/usr/bin/env python3
""" Module for 0-app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

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
    """ get_locale - gets locale in following order:
        1. Locale from URL parameters
        2. Locale from user settings
        3. Locale from request header
        4. Default locale
    """
    langs = app.config['LANGUAGES']
    if request.args.get('locale', None):
        if request.args.get('locale') in langs:
            return request.args.get('locale')
    if g.user and g.user['locale'] and g.user['locale'] in langs:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ get_timezone - gets timezone from:
        1. Find timezone parameter in URL parameters
        2. Find time zone from user settings
        3. Default to UTC"""
    if request.args.get('timezone', None):
        try:
            timezone(request.args.get('timezone'))
            return request.args.get('timezone')
        except UnknownTimeZoneError as e:
            return "UTC"
    if g.user and g.user['timezone']:
        try:
            timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError as e:
            return "UTC"
    return "UTC"


@app.route("/")
def index():
    """ index - returns the index template """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
