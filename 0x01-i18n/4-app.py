#!/usr/bin/env python3
""" Module for 0-app """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
