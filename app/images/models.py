from app import db
from app.users.models import User

imagetagstable = db.Table("imagetags", db.Column("image", db.String(32), db.ForeignKey('images.imgname')),
                          db.Column("tag", db.Integer, db.ForeignKey('tags.tagid')))


class Images(db.Model):
    __tablename__ = "images"
    imgname = db.Column(db.String(32), primary_key=True)
    contentlevel = db.Column(db.Integer, nullable=False)
    uploadtime = db.Column(db.DateTime, nullable=False)
    uploader = db.Column(db.String(32), db.ForeignKey(User.username), nullable=False)
    tags = db.relationship('Tags', secondary=imagetagstable, backref="tagimages")

    def __init__(self, imgname, contentlevel, uploadtime, uploader):
        self.imgname = imgname
        self.contentlevel = contentlevel
        self.uploadtime = uploadtime
        self.uploader = uploader

    def __repr__(self):
        return "<Image %r>" % self.imgname


class Tags(db.Model):
    __tablename__ = "tags"
    tagid = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(32), nullable=False)
    tagnamespace = db.Column(db.String(32), nullable=False)

    def __init__(self, tagname, tagnamespace):
        self.tagname = tagname
        self.tagnamespace = tagnamespace

    def __repr__(self):
        return "<Tag %r>" % self.tagname