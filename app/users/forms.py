from flask_wtf import Form
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    remember_me = BooleanField("Remember Me", default=False)
