from flask import Blueprint, g, redirect, request, url_for
from flask_login import login_required, logout_user

from .models import User
from .utils import handlelogin
from app import lm


mod = Blueprint('users', __name__, url_prefix="/users")


@lm.user_loader
def load_user(uid):
    return User.query.get(int(uid))


@mod.route('/login', methods=['POST'])
def login():
    if g.user is None or g.user.is_anonymous():
        handlelogin(request.form['username'], request.form['password'],
                    request.form['remember_me'] if 'remember_me' in request.form else False)
    return redirect(url_for('home'))


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))