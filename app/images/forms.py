from flask_wtf import Form
from wtforms.fields import FileField, RadioField, TextAreaField
from wtforms.validators import Optional

from app import app


class ImageUploadForm(Form):
    image = FileField("Image")
    contentlevel = RadioField("Content Level", choices=app.config["CONTENTLEVELS"], coerce=int, default=0)
    tagfield = TextAreaField("Tags", [Optional()])