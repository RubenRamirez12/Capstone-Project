from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from .playlist import playlist_songs


class Song(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("albums.id")), nullable=False
    )
    artist_name = db.Column(db.String(255), nullable=False)
    song_url = db.Column(db.String(500), nullable=False)
    song_length = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    album = db.relationship("Album", backref="songs")
    included_playlist = db.relationship("Playlist", secondary=playlist_songs, backref="included_songs")

    def to_dict(self, timestamps=False):
        dct = {
            "id": self.id,
            "albumId": self.album_id,
            "artistName": self.artist_name,
            "songUrl": self.song_url,
            "song_length": self.song_length,
            "image": self.image,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at
