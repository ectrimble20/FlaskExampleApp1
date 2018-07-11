import os


class Config(object):
    """
    Defaults configuration object, adjust these using Env vars.
    """
    ENV = os.environ.get('FLASK_ENV', 'production')
    DEBUG = os.environ.get('FLASK_DEBUG', False)
    TESTING = os.environ.get('FLASK_TESTING', False)
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # this should pretty much always be false
    APPLICATION_ROOT = os.environ.get('FLASK_APPLICATION_ROOT', '/')
