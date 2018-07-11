from datetime import datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from www.config import Config
from www.database import database

crypt = Bcrypt()
login_manager = LoginManager()


def create_application(configuration):
    application = Flask(__name__)
    with application.app_context():
        application.config.from_object(configuration)
        database.init_app(application)
        # attempt to create the database, this defaults to checking if exists prior to create so we can
        # safely run this prior to execution.
        from www.model import User, Forum, LoginAudit, Topic, Reply
        database.create_all()
        crypt.init_app(application)
        login_manager.init_app(application)
        # load blue prints
        # we import here because some things don't exist until the application exists
        from www.router import runtime
        application.register_blueprint(runtime)
        # register blue prints
        # application.register_blueprint(users)
    return application


def logger(state='UNKNOWN', message='No Message'):
    ts = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    print("<{}>{}:{}".format(ts, state.upper(), message))
