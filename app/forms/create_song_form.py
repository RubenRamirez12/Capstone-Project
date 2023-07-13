from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired
from ..api.aws_helpers import ALLOWED_AUDIO_EXTENSIONS

class CreateSongForm(FlaskForm):
    album_id = IntegerField("album_id", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    song = FileField("song", validators=[FileAllowed(list(ALLOWED_AUDIO_EXTENSIONS))])
    submit = SubmitField("Submit")
