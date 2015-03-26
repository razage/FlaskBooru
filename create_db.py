from app import db
from app.users.models import User
from app.images.models import Images, Tags

db.create_all()
db.session.commit()

db.session.add(User("admin", "password", 1))
db.session.add(Tags("tagme", "system"))
db.session.add(Tags("reported", "system"))
db.session.commit()