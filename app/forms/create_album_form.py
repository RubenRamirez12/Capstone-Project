from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired
from ..api.aws_helpers import ALLOWED_IMAGE_EXTENSIONS

class CreateAlbumForm(FlaskForm):
    artist_id = IntegerField("artist_id", validators=[])
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description",validators=[DataRequired()])
    image = FileField("image", validators=[FileRequired(), FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
    submit = SubmitField("Submit")
