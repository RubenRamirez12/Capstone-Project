from flask import Blueprint, request
from flask_login import current_user, login_required
from ..models import User, Album, db, Song
from ..forms import EditAlbumForm, CreateSongForm
from .aws_helpers import get_unique_filename, upload_file_to_s3
from .auth_routes import validation_errors_to_error_messages


album_routes = Blueprint("albums", __name__)


@album_routes.route("/getAll")
def get_all_playlists():
    all_albums_query = Album.query.all()

    all_albums = [album.to_dict() for album in all_albums_query]

    return {"albums": all_albums}


@album_routes.route("/getOne/<int:albumId>")
def get_one_album(albumId):
    album = Album.query.get(albumId)

    return {"album": album.to_dict_single()}


@album_routes.route("/edit/<int:albumId>", methods=["PUT"])
@login_required
def edit_album(albumId):
    form = EditAlbumForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        album = Album.query.get(albumId)

        if album is None or album.artist_id != current_user.id:
            return {"errors": "Album not found"}, 404

        if form.data["image"] is not None:
            image = form.data["image"]
            image.filename = get_unique_filename(image.filename)
            upload = upload_file_to_s3(image)

            if "url" not in upload:
                return {ERROR: "HERE IS ERROR"}
            album.image_url = upload["url"]

        album.name = form.data["name"]
        album.description = form.data["description"]

        db.session.commit()

        return album.to_dict_single()

    return {"errors": validation_errors_to_error_messages(form.errors)}, 401


@album_routes.route("/<int:albumId>/song", methods=["POST"])
@login_required
def create_album_song(albumId):
    form = CreateSongForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        album = Album.query.get(albumId)

        if album is None or album.artist_id != current_user.id:
            return {"errors": "Album not found"}, 404

            song = form.data["song"]
            song.filename = get_unique_filename(song.filename)
            upload = upload_file_to_s3(song)

            if "url" not in upload:
                return {ERROR: "HERE IS ERROR"}

        # newSong = Song(
        #     album_id=form.data["album_id"],
        #     name=form.data["name"],
        #     song_url=upload["url"],
        # )

        # db.session.add(newSong)
        # db.session.commit()

        # return newSong.to_dict()
        return {}

    return {"errors": validation_errors_to_error_messages(form.errors)}, 401
