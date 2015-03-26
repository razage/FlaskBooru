from hashlib import md5
from os.path import join
from shutil import move

from PIL import Image
from sqlalchemy.orm.exc import NoResultFound

from .models import Tags
from app import app, db


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config["ALLOWEDTYPES"]


def applytags(image, taglist):
    print(taglist)
    alltags = db.session.query(Tags)
    for t in range(len(taglist)):
        try:
            _test = alltags.filter(Tags.tagname == taglist[t][1]).one()
            image.tags.append(_test)
        except NoResultFound:
            db.session.add(Tags(taglist[t][1], taglist[t][0]))
            db.session.commit()
            image.tags.append(alltags.filter(Tags.tagname == taglist[t][1]).one())
            db.session.commit()


def getimagehash(image):
    return md5(image).hexdigest()


def makethumbnail(image):
    img = Image.open(join(app.config["IMAGEFOLDER"], image))
    img.thumbnail((200, 200), Image.ANTIALIAS)
    img.save(join(app.config["THUMBFOLDER"], image))


def moveimage(sourcename, destinationname):
    move(join(app.config["IMAGETEMP"], sourcename), join(app.config["IMAGEFOLDER"], destinationname))


def parsetags(rawtags):
    _pass1 = rawtags.split(" ")
    _pass2 = []
    for i in range(len(_pass1)):
        _tmptagpair = _pass1[i].split(":")
        if len(_tmptagpair) is 1:
            _pass2.append(["general", _tmptagpair[0].lower()])
        else:
            if _tmptagpair[0] in app.config["NAMESPACES"]:
                _pass2.append([_tmptagpair[0].lower(), _tmptagpair[1].lower()])
    return _pass2