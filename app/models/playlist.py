from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from .playlist_songs import playlist_songs


class Playlist(db.Model):
    __tablename__ = "playlists"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500))
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    owner = db.relationship("User", back_populates="playlists")

    songs = db.relationship(
        "Song", secondary=playlist_songs, back_populates="playlists"
    )

    def to_dict(self, timestamps=False):
        dct = {
            "id": self.id,
            "description": self.description,
            "image": self.image,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at
