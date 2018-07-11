from flask import Blueprint, render_template, jsonify, url_for, flash, redirect, request, current_app, Response
from flask_login import login_required, current_user, login_user, logout_user
from www import crypt, logger
from www.database import database
from www.forms.user import UserRegistration, UserLoginForm
from www.model import User


runtime = Blueprint('runtime', __name__)


@runtime.route('/health', methods=["GET"])
def health_check():
    return Response(status=200)


@runtime.route('/', methods=["GET"])
def index():
    return render_template('index.html', title="Index")


@runtime.route('/login', methods=["GET", "POST"])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('runtime.index'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not crypt.check_password_hash(user.password, form.password.data):
            flash("Login Failed", "danger")
            logger(state="WARNING", message="Failed Login Attempt From {}".format(request.remote_addr))
            return render_template("user_login.html", title="Login")
        else:
            # successful login
            login_user(user, remember=form.remember.data)
            logger(state="INFO", message="Successful Login by {} From {}"
                   .format(user.display_name, request.remote_addr))
            flash("Welcome {}".format(user.display_name), "success")
            return redirect(url_for('runtime.index'))
    else:
        return render_template('user_login.html', title="Login", form=form)


@runtime.route('/logout', methods=["GET"])
def user_logout():
    if current_user.is_authenticated:
        logger(state="INFO", message="User {} logged out".format(current_user.display_name))
        logout_user()
        flash("Logged Out Successfully", "success")
    return redirect(url_for('runtime.index'))


@runtime.route('/registration', methods=["GET", "POST"])
def user_register():
    form = UserRegistration()
    if form.validate_on_submit():
        password_hash = crypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            email=form.email.data,
            password=password_hash,
            display_name=form.display_name.data
        )
        database.session.add(user)
        database.session.commit()
        flash("Registration Successful, please login to continue", "success")
        logger(state="INFO", message="User account for {} created".format(form.email.data))
        return redirect(url_for('runtime.user_login'))
    else:
        return render_template('user_register.html', title="Register Account", form=form)


@runtime.route('/user', methods=["GET", "PUT", "POST"])
def user_profile():
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/admin', methods=["GET", "PUT", "POST"])
def admin_index():
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/admin/user/<int:id>', methods=["GET", "PUT", "POST"])
@runtime.route('/admin/user', methods=["GET", "PUT", "POST"])
def admin_users(id=None):
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/admin/forum/<int:id>', methods=["GET", "PUT", "POST"])
@runtime.route('/admin/forum', methods=["GET", "PUT", "POST"])
def admin_forums(id=None):
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/admin/post/<int:id>', methods=["GET", "PUT", "POST"])
@runtime.route('/admin/post', methods=["GET", "PUT", "POST"])
def admin_posts(id=None):
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/admin/reply/<int:id>', methods=["GET", "PUT", "POST"])
@runtime.route('/admin/reply', methods=["GET", "PUT", "POST"])
def admin_replies(id=None):
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/forum', methods=["GET", "POST"])
def forum():
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/post', methods=["GET", "POST"])
def post():
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))


@runtime.route('/reply', methods=["GET", "POST"])
def reply():
    flash("Feature Not Implemented Yet", "info")
    return redirect(url_for('runtime.index'))
