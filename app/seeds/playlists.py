from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy.sql import text


def seed_playlists():
    playlist1 = Playlist(owner_id = 1, owner_name="Demo", name="personal favorites", description="A bunch of songs that i like")
    playlist2 = Playlist(owner_id = 1, owner_name="Demo", name="rap music", description="Rap Songs I like")


    db.session.add(playlist1)
    db.session.add(playlist2)

    db.session.commit()


def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()
