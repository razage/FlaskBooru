from werkzeug.security import generate_password_hash

from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)
    userimages = db.relationship("Images", backref="users")

    def __init__(self, username, password, role=0):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username