from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

playlist_songs = db.Table(
    "playlist_songs",
    db.metadata,
    db.Column(
        "playlist_id", db.Integer, db.ForeignKey("playlists.id"), primary_key=True
    ),
    db.Column("song_id", db.Integer, db.ForeignKey("songs.id"), primary_key=True),
)


class Playlist(db.Model):
    __tablename__ = "playlists"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    owner_name = db.Column(db.String(255), nullable=False)
    name = db.Column(
        db.String(255),
    )
    description = db.Column(db.String(500))
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    owner = db.relationship("User", back_populates="playlists")
    included_songs = db.relationship("Song", secondary=playlist_songs, backref="included_playlists")

    def to_dict(self, timestamps=False):
        dct = {
            "id": self.id,
            "ownerId": self.owner_id,
            "description": self.description,
            "image": self.image,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at
