from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from ..api.aws_helpers import ALLOWED_IMAGE_EXTENSIONS

class EditPlaylistForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description",validators=[DataRequired()])
    image = FileField("image", validators=[FileAllowed(ALLOWED_IMAGE_EXTENSIONS, "Not a allowed Image extension")])
    submit = SubmitField("Submit")
