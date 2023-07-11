from app.models import db, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_albums():
    album1 = Album(
        owner_id=2, artist_name="Tevvez", name="Phantom", description="Album by Tevvez"
    )
    album2 = Album(
        owner_id=3,
        artist_name="Lil Uzi Vert",
        name="Eternal Atake",
        description="Album by Lil Uzi Vert",
    )
    album3 = Album(
        owner_id=4,
        artist_name="Juice WRLD",
        name="Goodbye & Good Riddance",
        description="Album by JuiceWRLD",
    )
    album4 = Album(
        owner_id=5, artist_name="Avicii", name="Stories", description="Album by Avicii"
    )

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)

    db.session.commit()


def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()
