from app.models import db, Song, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_songs():

    song_Avicii_1 = Song(
        album_id = 4,
        name = "Waiting For Love",
        song_url = "randomURL"
    )
    song_Avicii_2 = Song(
        album_id = 4,
        name = "Talk To Myself",
        song_url = "randomURL"
    )
    song_Avicii_3 = Song(
        album_id = 4,
        name = "Touch Me",
        song_url = "randomURL"
    )
    song_Avicii_4 = Song(
        album_id = 4,
        name = "Ten More Days",
        song_url = "randomURL"
    )
    song_Avicii_5 = Song(
        album_id = 4,
        name = "For A Better Day",
        song_url = "randomURL"
    )
    song_Avicii_6 = Song(
        album_id = 4,
        name = "Broken Arrows",
        song_url = "randomURL"
    )
    song_Avicii_7 = Song(
        album_id = 4,
        name = "True Believer",
        song_url = "randomURL"
    )
    song_Avicii_8 = Song(
        album_id = 4,
        name = "City Lights",
        song_url = "randomURL"
    )
    song_Avicii_9 = Song(
        album_id = 4,
        name = "Pure Grinding",
        song_url = "randomURL"
    )
    song_Avicii_10 = Song(
        album_id = 4,
        name = "Sunset Jesus",
        song_url = "randomURL"
    )
    song_Avicii_11 = Song(
        album_id = 4,
        name = "Can't Catch Me",
        song_url = "randomURL"
    )
    song_Avicii_12 = Song(
        album_id = 4,
        name = "Somewhere in Stockholm",
        song_url = "randomURL"
    )
    song_Avicii_13 = Song(
        album_id = 4,
        name = "Trouble",
        song_url = "randomURL"
    )
    song_Avicii_14 = Song(
        album_id = 4,
        name = "Gonna Love Ya",
        song_url = "randomURL"
    )

    song_Tevvez_1 = Song(
        album_id = 1,
        name = "Vision",
        song_url = "randomURL"
    )
    song_Tevvez_2 = Song(
        album_id = 1,
        name = "Back in time",
        song_url = "randomURL"
    )
    song_Tevvez_3 = Song(
        album_id = 1,
        name = "In my dream",
        song_url = "randomURL"
    )
    song_Tevvez_4 = Song(
        album_id = 1,
        name = "Mystique, Pt. 2",
        song_url = "randomURL"
    )
    song_Tevvez_5 = Song(
        album_id = 1,
        name = "Infinity",
        song_url = "randomURL"
    )
    song_Tevvez_6 = Song(
        album_id = 1,
        name = "Guardian Angel",
        song_url = "randomURL"
    )
    song_Tevvez_7 = Song(
        album_id = 1,
        name = "Frozen in time",
        song_url = "randomURL"
    )
    song_Tevvez_8 = Song(
        album_id = 1,
        name = "Light",
        song_url = "randomURL"
    )
    song_Tevvez_9 = Song(
        album_id = 1,
        name = "Legend",
        song_url = "randomURL"
    )
    song_Tevvez_10 = Song(
        album_id = 1,
        name = "Legacy",
        song_url = "randomURL"
    )
    song_Tevvez_11 = Song(
        album_id = 1,
        name = "Lost",
        song_url = "randomURL"
    )
    song_Tevvez_12 = Song(
        album_id = 1,
        name = "Oblivion",
        song_url = "randomURL"
    )

    song_JuiceWRLD_1 = Song(
        album_id = 3,
        name = "Intro",
        song_url = "randomURL"
    )
    song_JuiceWRLD_2 = Song(
        album_id = 3,
        name = "All Girls Are The Same",
        song_url = "randomURL"
    )
    song_JuiceWRLD_3 = Song(
        album_id = 3,
        name = "Lucid Dreams",
        song_url = "randomURL"
    )
    song_JuiceWRLD_4 = Song(
        album_id = 3,
        name = "Wasted (feat. Lil Uzi Vert)",
        song_url = "randomURL"
    )
    song_JuiceWRLD_5 = Song(
        album_id = 3,
        name = "Armed And Dangerous",
        song_url = "randomURL"
    )
    song_JuiceWRLD_6 = Song(
        album_id = 3,
        name = "Black & White",
        song_url = "randomURL"
    )
    song_JuiceWRLD_7 = Song(
        album_id = 3,
        name = "Lean Wit Me",
        song_url = "randomURL"
    )
    song_JuiceWRLD_8 = Song(
        album_id = 3,
        name = "I'll Be Fine",
        song_url = "randomURL"
    )
    song_JuiceWRLD_9 = Song(
        album_id = 3,
        name = "Used To",
        song_url = "randomURL"
    )
    song_JuiceWRLD_10 = Song(
        album_id = 3,
        name = "Candles",
        song_url = "randomURL"
    )
    song_JuiceWRLD_11 = Song(
        album_id = 3,
        name = "Scared Of Love (with instrumental by Ghost Loft)",
        song_url = "randomURL"
    )
    song_JuiceWRLD_12 = Song(
        album_id = 3,
        name = "Hurt Me",
        song_url = "randomURL"
    )
    song_JuiceWRLD_13 = Song(
        album_id = 3,
        name = "I'm Still",
        song_url = "randomURL"
    )
    song_JuiceWRLD_14 = Song(
        album_id = 3,
        name = "End Of The Road",
        song_url = "randomURL"
    )
    song_JuiceWRLD_15 = Song(
        album_id = 3,
        name = "Long Gone",
        song_url = "randomURL"
    )

    song_LilUziVert_1 = Song(
        album_id = 2,
        name = "Baby Pluto",
        song_url = "randomURL"
    )
    song_LilUziVert_2 = Song(
        album_id = 2,
        name = "Lo Mein",
        song_url = "randomURL"
    )
    song_LilUziVert_3 = Song(
        album_id = 2,
        name = "Silly Watch",
        song_url = "randomURL"
    )
    song_LilUziVert_4 = Song(
        album_id = 2,
        name = "POP",
        song_url = "randomURL"
    )
    song_LilUziVert_5 = Song(
        album_id = 2,
        name = "You Better Move",
        song_url = "randomURL"
    )
    song_LilUziVert_6 = Song(
        album_id = 2,
        name = "Homecoming",
        song_url = "randomURL"
    )
    song_LilUziVert_7 = Song(
        album_id = 2,
        name = "I'm Sorry",
        song_url = "randomURL"
    )
    song_LilUziVert_8 = Song(
        album_id = 2,
        name = "Celebration Station",
        song_url = "randomURL"
    )
    song_LilUziVert_9 = Song(
        album_id = 2,
        name = "Bigger Than Life",
        song_url = "randomURL"
    )
    song_LilUziVert_10 = Song(
        album_id = 2,
        name = "Chrome Heart Tags",
        song_url = "randomURL"
    )
    song_LilUziVert_11 = Song(
        album_id = 2,
        name = "Bust Me",
        song_url = "randomURL"
    )
    song_LilUziVert_12 = Song(
        album_id = 2,
        name = "Prices",
        song_url = "randomURL"
    )
    song_LilUziVert_13 = Song(
        album_id = 2,
        name = " Urgency (feat. Syd)",
        song_url = "randomURL"
    )
    song_LilUziVert_14 = Song(
        album_id = 2,
        name = "Venetia",
        song_url = "randomURL"
    )
    song_LilUziVert_15 = Song(
        album_id = 2,
        name = "Secure The Bag",
        song_url = "randomURL"
    )
    song_LilUziVert_16 = Song(
        album_id = 2,
        name = "P2",
        song_url = "randomURL"
    )
    song_LilUziVert_17 = Song(
        album_id = 2,
        name = "Futsal Shuffle 2020 - Bonus Track",
        song_url = "randomURL"
    )
    song_LilUziVert_18 = Song(
        album_id = 2,
        name = "That Way - Bonus Track",
        song_url = "randomURL"
    )




    db.session.add(song_Avicii_1)
    db.session.add(song_Avicii_2)
    db.session.add(song_Avicii_3)
    db.session.add(song_Avicii_4)
    db.session.add(song_Avicii_5)
    db.session.add(song_Avicii_6)
    db.session.add(song_Avicii_7)
    db.session.add(song_Avicii_8)
    db.session.add(song_Avicii_9)
    db.session.add(song_Avicii_10)
    db.session.add(song_Avicii_11)
    db.session.add(song_Avicii_12)
    db.session.add(song_Avicii_13)
    db.session.add(song_Avicii_14)

    db.session.add(song_Tevvez_1)
    db.session.add(song_Tevvez_2)
    db.session.add(song_Tevvez_3)
    db.session.add(song_Tevvez_4)
    db.session.add(song_Tevvez_5)
    db.session.add(song_Tevvez_6)
    db.session.add(song_Tevvez_7)
    db.session.add(song_Tevvez_8)
    db.session.add(song_Tevvez_9)
    db.session.add(song_Tevvez_10)
    db.session.add(song_Tevvez_11)
    db.session.add(song_Tevvez_12)

    db.session.add(song_JuiceWRLD_1)
    db.session.add(song_JuiceWRLD_2)
    db.session.add(song_JuiceWRLD_3)
    db.session.add(song_JuiceWRLD_4)
    db.session.add(song_JuiceWRLD_5)
    db.session.add(song_JuiceWRLD_6)
    db.session.add(song_JuiceWRLD_7)
    db.session.add(song_JuiceWRLD_8)
    db.session.add(song_JuiceWRLD_9)
    db.session.add(song_JuiceWRLD_10)
    db.session.add(song_JuiceWRLD_11)
    db.session.add(song_JuiceWRLD_12)
    db.session.add(song_JuiceWRLD_13)
    db.session.add(song_JuiceWRLD_14)
    db.session.add(song_JuiceWRLD_15)

    db.session.add(song_LilUziVert_1)
    db.session.add(song_LilUziVert_2)
    db.session.add(song_LilUziVert_3)
    db.session.add(song_LilUziVert_4)
    db.session.add(song_LilUziVert_5)
    db.session.add(song_LilUziVert_6)
    db.session.add(song_LilUziVert_7)
    db.session.add(song_LilUziVert_8)
    db.session.add(song_LilUziVert_9)
    db.session.add(song_LilUziVert_10)
    db.session.add(song_LilUziVert_11)
    db.session.add(song_LilUziVert_12)
    db.session.add(song_LilUziVert_13)
    db.session.add(song_LilUziVert_14)
    db.session.add(song_LilUziVert_15)
    db.session.add(song_LilUziVert_16)
    db.session.add(song_LilUziVert_17)
    db.session.add(song_LilUziVert_18)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))

    db.session.commit()
