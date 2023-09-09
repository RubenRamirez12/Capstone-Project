from app.models import db, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_albums():
    album1 = Album(
        artist_id=2,
        name="Phantom",
        description="Album by Tevvez",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/Phantom-Tevvez.jpeg",
        single=False,
    )
    album2 = Album(
        artist_id=3,
        name="Eternal Atake",
        description="Album by Lil Uzi Vert",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/Eternal_Atake_Lil_Uzi_Vert.jpg",
        single=False,
    )
    album3 = Album(
        artist_id=4,
        name="Goodbye & Good Riddance",
        description="Album by JuiceWRLD",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/G%26GR-juiceWrld.png",
        single=False,
    )
    album4 = Album(
        artist_id=5,
        name="Stories",
        description="Album by Avicii",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/Stories-Avicii.png",
        single=False,
    )
    album5= Album(
        artist_id=6,
        name="Future Nostalgia",
        description="Album by Dua Lipa",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/DuaLipaPFP.jpeg",
        single=False,
    )
    album6 = Album(
        artist_id=3,
        name="Luv Is Rage 2 (Deluxe)",
        description="Album by Lil Uzi Vert",
        image_url="https://groovify-bucket.s3.us-west-1.amazonaws.com/LuvIsRage21.jpg",
        single=False,
    )

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.add(album6)

    db.session.commit()


def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()
