from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from .playlist_songs import playlist_songs


class Song(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("albums.id")), nullable=False
    )
    name = db.Column(db.String(200), nullable=False)
    song_url = db.Column(db.String(500), nullable=False)
    song_length = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    album = db.relationship("Album", back_populates="songs")

    playlists = db.relationship(
        "Playlist", secondary=playlist_songs, back_populates="songs"
    )

    def to_dict(self, timestamps=False):
        album = self.album
        artist = album.artist
        dct = {
            "id": self.id,
            "albumId": self.album_id,
            "artistId": artist.id,
            "albumImg": album.image_url,
            "artistName": artist.username,
            "name": self.name,
            "songUrl": self.song_url,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at

        return dct
