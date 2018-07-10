from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from www.model import User


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UserRegistration(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    email_confirm = StringField('Confirm Email', validators=[EqualTo('email')])
    display_name = StringField('Display Name', validators=[Length(min=2, max=40), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8, max=20), DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField("Register Account")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email address is already in use, please use a different email address.")


class UserDisplayNameUpdate(FlaskForm):
    display_name = StringField('Display Name', validators=[Length(min=2, max=40), DataRequired()])
    submit = SubmitField("Update Display Name")


class UserPasswordUpdate(FlaskForm):
    password = PasswordField('Change Password', validators=[Length(min=8, max=20), DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField("Update Password")


class UserCloseAccountForm(FlaskForm):
    confirm = BooleanField("Close Account")
    submit = SubmitField('Confirm Account Closure')
