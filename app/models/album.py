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
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    single = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    artist = db.relationship("User", back_populates="albums")
    songs = db.relationship("Song", back_populates="album", cascade='all, delete')

    def to_dict(self, timestamps=False):
        dct = {
            "id": self.id,
            "artistId": self.artist_id,
            "artistName": self.artist_name,
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "single": self.single,
        }

        if timestamps:
            dct["createdAt"] = self.created_at
            dct["updatedAt"] = self.updated_at
