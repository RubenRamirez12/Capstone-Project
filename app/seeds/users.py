from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(username="Demo", email="demo@aa.io", password="password", profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/icon-user.png")
    tevvez = User(username="Tevvez", email="tevvez@aa.io", password="password", profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/TevvezPfp.jpeg")
    lilUzi = User(username="Lil Uzi Vert", email="lilUzi@aa.io", password="password", profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/liluziPfp.jpeg")
    juiceWRLD = User(username="Juice WRLD", email="juiceWRLD@aa.io", password='password', profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/JuiceWrldPfp.jpeg")
    avicii = User(username="Avicii", email="avicii@aa.io", password='password', profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/AviciiPfp.jpeg")
    duaLipa = User(username="Dua Lipa", email="duaLipa@aa.io" , password='password', profile_pic="https://groovify-bucket.s3.us-west-1.amazonaws.com/DuaLipaPFP.jpeg")



    db.session.add(demo)
    db.session.add(tevvez)
    db.session.add(lilUzi)
    db.session.add(juiceWRLD)
    db.session.add(avicii)
    db.session.add(duaLipa)

    db.session.commit()

    # Future Nostalga Dua Lipa



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
