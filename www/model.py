from datetime import datetime
from www.database import database
from www import login_manager
from flask_login import UserMixin

"""
User - login access
LoginAudit - logs successful and unsuccessful login attempts
Forum - Top level discussion board
Topic - Post top level
Reply - Replies attached to a post.
"""


@login_manager.user_loader
def load_user(user_id):  # TODO fix this
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)
    display_name = database.Column(database.String(60), nullable=True)
    is_active = database.Column(database.Boolean, nullable=False, default=True)
    is_admin = database.Column(database.Boolean, nullable=False, default=False)
    record_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


class LoginAudit(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=True)
    remote_ip = database.Column(database.String(16), nullable=False)
    result = database.Column(database.String(16), nullable=False)
    result_note = database.Column(database.String(255), nullable=True)
    record_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


class Forum(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    end_point = database.Column(database.String(45), unique=True, nullable=False)
    description = database.Column(database.String(255), nullable=False)
    owner_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    is_active = database.Column(database.Boolean, nullable=False, default=True)
    record_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


class Topic(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    end_point = database.Column(database.String(45), unique=True, nullable=False)
    author_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    forum_id = database.Column(database.Integer, database.ForeignKey('forum.id'), nullable=False)
    is_active = database.Column(database.Boolean, nullable=False, default=True)
    record_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


class Reply(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    end_point = database.Column(database.String(45), unique=True, nullable=False)
    author_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    topic_id = database.Column(database.Integer, database.ForeignKey('topic.id'), nullable=False)
    is_active = database.Column(database.Boolean, nullable=False, default=True)
    record_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
