from datetime import datetime
from os import remove
from os.path import join

from flask import Blueprint, flash, render_template, redirect, request, url_for
from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename

from .forms import ImageUploadForm
from .models import Images
from .utils import allowed_file, applytags, getimagehash, makethumbnail, moveimage, parsetags
from app import app, db


mod = Blueprint('images', __name__, url_prefix="/images")


@mod.route("/")
def imagehomeredirect():
    return redirect(url_for("images.imageindex", page=1))


@mod.route("/<int:page>")
def imageindex(page):
    images = db.session.query(Images).order_by(desc(Images.uploadtime)).offset(app.config["IMAGESPERPAGE"] * (page - 1)).limit(app.config["IMAGESPERPAGE"])
    return render_template("images/imageindex.html", title="FlaskBooru - Page %s" % page, images=images)

@mod.route("/upload", methods=["GET", "POST"])
def upload():
    form = ImageUploadForm()
    if form.validate_on_submit():
        img = request.files['image']
        if img and allowed_file(img.filename.lower()):
            tmpfilename = secure_filename(img.filename)
            img.save(join(app.config["IMAGETEMP"], tmpfilename))
            finalname = "%s.%s" % (getimagehash(open(join(app.config["IMAGETEMP"], tmpfilename), 'rb').read()), tmpfilename.split(".")[1])
            try:
                check = db.session.query(Images).filter(Images.imgname == finalname).one()
            except NoResultFound:
                db.session.add(Images(finalname, form.contentlevel.data, datetime.now(), "admin"))
                db.session.commit()
                moveimage(tmpfilename, finalname)
                imagefortagging = db.session.query(Images).filter(Images.imgname == finalname).one()
                applytags(imagefortagging, parsetags(form.tagfield.data))
                makethumbnail(finalname)
                return redirect(url_for("images.upload"))
            remove(join(app.config["IMAGETEMP"], tmpfilename))
            flash("This image is already on the booru.")
            return redirect(url_for("images.upload"))
        else:
            print("Forbidden extension!")
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in field %s - %s" % (getattr(form, field).label.text, error))
    return render_template("images/upload.html", title="Upload Image", form=form)