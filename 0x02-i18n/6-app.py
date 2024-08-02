#!/usr/bin/env python3
"""
Flask project
"""
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Get user attribute 
    """
    return users.get(int(id), {})


@babel.localeselector
def get_locale() -> str:
    """
    Gets local obj
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for loc in options:
        if loc and loc in Config.LANGUAGES:
            return loc


@app.before_request
def before_request() -> None:
    """
    Add session
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render 6 index
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
