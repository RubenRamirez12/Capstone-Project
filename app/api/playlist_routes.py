from flask import Blueprint
from flask_login import current_user, login_required
from ..models import User, Playlist, db, Song

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/create')
@login_required
def create_playlist():
    new_playlist = Playlist(
        owner_id = current_user.id,
        name = f"My Playlist #{len(current_user.playlists) + 1}",
        image_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/No+playlist+image.png"
    )
    db.session.add(new_playlist)
    db.session.commit()

    return new_playlist.to_dict()

@playlist_routes.route('/getAll')
@login_required
def get_all_playlists():
    all_playlists = [playlist.to_dict() for playlist in current_user.playlists]

    return { "playlists": all_playlists }

@playlist_routes.route('/<int:playlistId>')
def get_playlist(playlistId):
    playlist = Playlist.query.get(playlistId)

    return playlist.to_dict_with_songs()

@playlist_routes.route('/addSong/<int:playlistId>/<int:songId>')
@login_required
def add_song_to_playlist(playlistId, songId):
    playlist = Playlist.query.get(playlistId)
    if (playlist.owner_id != current_user.id):
        return { "errors": "You do not have permission to edit this playlist." }

    song = Song.query.get(songId)

    playlist.songs.append(song)
    db.session.commit()

    return playlist.to_dict_with_songs()
