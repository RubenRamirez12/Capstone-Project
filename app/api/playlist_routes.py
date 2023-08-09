from flask import Blueprint, request
from flask_login import current_user, login_required
from ..models import User, Playlist, db, Song
from ..forms import EditPlaylistForm
from .aws_helpers import get_unique_filename, upload_file_to_s3
from .auth_routes import validation_errors_to_error_messages

playlist_routes = Blueprint("playlists", __name__)


@playlist_routes.route("/create")
@login_required
def create_playlist():
    new_playlist = Playlist(
        owner_id=current_user.id,
        name=f"My Playlist #{len(current_user.playlists) + 1}",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/No+playlist+image.png",
        description="",
    )
    db.session.add(new_playlist)
    db.session.commit()

    return new_playlist.to_dict()


@playlist_routes.route("/getAll")
@login_required
def get_all_playlists():
    all_playlists = [playlist.to_dict() for playlist in current_user.playlists]

    return {"playlists": all_playlists}


@playlist_routes.route("/<int:playlistId>")
def get_playlist(playlistId):
    playlist = Playlist.query.get(playlistId)

    return playlist.to_dict_with_songs()


@playlist_routes.route("/addSong/<int:playlistId>/<int:songId>")
@login_required
def add_song_to_playlist(playlistId, songId):
    playlist = Playlist.query.get(playlistId)
    if playlist.owner_id != current_user.id:
        return {"errors": "You do not have permission to edit this playlist."}

    song = Song.query.get(songId)

    playlist.songs.append(song)
    db.session.commit()

    return playlist.to_dict_with_songs()


@playlist_routes.route("/delete/<int:playlistId>", methods=["DELETE"])
@login_required
def delete_playlist(playlistId):
    playlist = Playlist.query.get(playlistId)
    if playlist.owner_id != current_user.id:
        return {"errors": "You do not have permission to edit this playlist."}

    db.session.delete(playlist)
    db.session.commit()

    return {"message": "Playlist successfully deleted."}


@playlist_routes.route("/edit/<int:playlistId>", methods=["PUT"])
@login_required
def edit_playlist(playlistId):
    form = EditPlaylistForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        playlist = Playlist.query.get(playlistId)

        if playlist is None or playlist.owner_id != current_user.id:
            return {"errors": "You do not have permission to edit this playlist."}

        if form.data["image"] is not None:
            image = form.data["image"]
            image.filename = get_unique_filename(image.filename)
            upload = upload_file_to_s3(image)

            if "url" not in upload:
                return {"errors": "Error uploading image."}
            playlist.image_url = upload["url"]

        playlist.name = form.data["name"]
        playlist.description = form.data["description"]

        db.session.commit()

        return {"single": playlist.to_dict_with_songs(), "all": playlist.to_dict()}

    return {"errors": validation_errors_to_error_messages(form.errors)}
