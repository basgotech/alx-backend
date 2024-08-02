#!/usr/bin/env python3
"""
Flask project
"""
import pytz
import datetime
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel
from flask_babel import format_datetime


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
    Add sessions
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))
    setattr(g, 'time', format_datetime(datetime.datetime.now()))

@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone from request object
    """
    get_time_zone = request.args.get('timezone', '').strip()
    if not get_time_zone and g.user:
        get_time_zone = g.user['timezone']
    try:
        get_time_zone = pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        get_time_zone = app.config['BABEL_DEFAULT_TIMEZONE']
    return get_time_zone

    
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render index
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
