from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class Album(db.Model):
    __tablename__ = "albums"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    single = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    artist = db.relationship("User", back_populates="albums")
    songs = db.relationship("Song", back_populates="album", cascade='all, delete')

    def to_dict(self, timestamps=False):
        artist = self.artist

        dct = {
            "id": self.id,
            "artistId": self.artist_id,
            "artistName": artist.username,
            "name": self.name,
            "description": self.description,
            "imageUrl": self.image_url,
            "single": self.single,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at

        return dct

    def to_dict_single(self, timestamps=False):
        artist = self.artist
        songs = [song.to_dict(timestamps=True) for song in self.songs]
        dct = {
            "id": self.id,
            "artistId": artist.id,
            "artistName": artist.username,
            "artistPic": artist.profile_pic,
            "name": self.name,
            "description": self.description,
            "imageUrl": self.image_url,
            "single": self.single,
            "songs": songs
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at

        return dct
