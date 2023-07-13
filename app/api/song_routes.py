from flask import Blueprint, request
from flask_login import current_user, login_required
from ..models import User, db, Song
from ..forms import EditSongForm
from .aws_helpers import get_unique_filename, upload_file_to_s3
from .auth_routes import validation_errors_to_error_messages

song_routes = Blueprint('songs', __name__)

@song_routes.route('/edit/<int:songId>', methods=["PUT"])
@login_required
def edit_song(songId):
    form = EditSongForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        current_song = Song.query.get(songId)

        if form.data["song"] is not None:
            new_song = form.data["song"]
            new_song.filename = get_unique_filename(new_song.filename)
            upload = upload_file_to_s3(new_song)

            if "url" not in upload:
                return {ERROR: "HERE IS ERROR"}

            current_song.song_url = upload["url"]

        current_song.name = form.data["name"]

        db.session.commit()

        return current_song.to_dict(timestamps=True)

    return {"errors": validation_errors_to_error_messages(form.errors)}, 401
