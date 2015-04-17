from flask import flash, redirect, request, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.users.models import User


def handlelogin(username, password, remember_me=False):
    user = User.query.filter(User.username == username).first()
    if user is not None:
        if check_password_hash(user.password, password):
            login_user(user, remember=remember_me)
            return redirect(request.args.get('next') or url_for('home'))
        else:
            flash("Incorrect login!", "error")
    else:
        flash("User doesn't exist!", "error")