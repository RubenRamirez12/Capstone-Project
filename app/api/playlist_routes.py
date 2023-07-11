from flask import Blueprint
from flask_login import current_user, login_required
from ..models import User, Playlist, db

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/create')
@login_required
def create_playlist():
    new_playlist = Playlist(
        owner_id = current_user.id,
        name = f"My Playlist #{len(current_user.playlists)}"
    )
    db.session.add(new_playlist)
    db.session.commit()

    return new_playlist.to_dict()

@playlist_routes.route('/getAll')
@login_required
def get_all_playlists():
    all_playlists = [playlist.to_dict() for playlist in current_user.playlists]

    return { "playlists": all_playlists }
