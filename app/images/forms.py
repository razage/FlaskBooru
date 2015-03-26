from flask_wtf import Form
from wtforms.fields import FileField, SelectField, TextAreaField
from wtforms.validators import Optional

from app import app


class ImageUploadForm(Form):
    image = FileField("Image")
    contentlevel = SelectField("Content Level", choices=app.config["CONTENTLEVELS"], coerce=int)
    tagfield = TextAreaField("Tags", [Optional()])