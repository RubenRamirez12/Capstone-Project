from flask import Blueprint
from flask_login import current_user
from ..models import User, Album, db

album_routes = Blueprint('albums', __name__)

@album_routes.route('/getAll')
def get_all_playlists():
    all_albums_query = Album.query.all()

    all_albums = [album.to_dict() for album in all_albums_query]

    return { "albums": all_albums }
