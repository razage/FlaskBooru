from flask import abort, flash, g, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from . import mod
from .forms import LoginForm
from .models import User
from app import app, db, lm


@lm.user_loader
def load_user(uid):
    return User.query.get(int(uid))


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is not None:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('home'))
            else:
                flash("Incorrect login!", "error")
                print("Incorrect login!")
        else:
            flash("User doesn't exist!", "error")
            print("User doesn't exist")
    return render_template("users/login.html", title="Login", form=form)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))