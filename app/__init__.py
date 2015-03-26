from flask import Flask, g, render_template
from flask_login import current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager(app)
lm.login_view = 'users.login'


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def home():
    return render_template("home.html", title="Index")


from app.images.views import mod as imagemod
from app.users import mod as usermod

app.register_blueprint(imagemod)
app.register_blueprint(usermod)