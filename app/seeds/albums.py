from app.models import db, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_albums():
    album1 = Album(
        artist_id=2,
        name="Phantom",
        description="Album by Tevvez",
        image="TEST",
        single=False,
    )
    album2 = Album(
        artist_id=3,
        name="Eternal Atake",
        description="Album by Lil Uzi Vert",
        image="TEST",
        single=False,
    )
    album3 = Album(
        artist_id=4,
        name="Goodbye & Good Riddance",
        description="Album by JuiceWRLD",
        image="TEST",
        single=False,
    )
    album4 = Album(
        artist_id=5,
        name="Stories",
        description="Album by Avicii",
        image="TEST",
        single=False,
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
