from app.models import db, Song, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_songs():

    song_Avicii_1 = Song(
        album_id = 4,
        name = "Waiting For Love",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/01+Waiting+For+Love.mp3"
    )
    song_Avicii_2 = Song(
        album_id = 4,
        name = "Talk To Myself",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/02+Talk+To+Myself.mp3"
    )
    song_Avicii_3 = Song(
        album_id = 4,
        name = "Touch Me",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/03+Touch+Me.mp3"
    )
    song_Avicii_4 = Song(
        album_id = 4,
        name = "Ten More Days",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/04+Ten+More+Days.mp3"
    )
    song_Avicii_5 = Song(
        album_id = 4,
        name = "For A Better Day",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/05+For+a+Better+Day.mp3"
    )
    song_Avicii_6 = Song(
        album_id = 4,
        name = "Broken Arrows",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/06+Broken+Arrows.mp3"
    )
    song_Avicii_7 = Song(
        album_id = 4,
        name = "True Believer",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/07+True+Believer.mp3"
    )
    song_Avicii_8 = Song(
        album_id = 4,
        name = "City Lights",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/08+City+Lights.mp3"
    )
    song_Avicii_9 = Song(
        album_id = 4,
        name = "Pure Grinding",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/09+Pure+Grinding+-.mp3"
    )
    song_Avicii_10 = Song(
        album_id = 4,
        name = "Sunset Jesus",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/10+Sunset+Jesus.mp3"
    )
    song_Avicii_11 = Song(
        album_id = 4,
        name = "Can't Catch Me",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/11+Can't+Catch+Me.mp3"
    )
    song_Avicii_12 = Song(
        album_id = 4,
        name = "Somewhere in Stockholm",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/12+Somewhere+In+Stockholm.mp3"
    )
    song_Avicii_13 = Song(
        album_id = 4,
        name = "Trouble",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/13+Trouble.mp3"
    )
    song_Avicii_14 = Song(
        album_id = 4,
        name = "Gonna Love Ya",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/14+Gonna+Love+Ya.mp3"
    )

    song_Tevvez_1 = Song(
        album_id = 1,
        name = "Vision",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Vision.mp3"
    )
    song_Tevvez_2 = Song(
        album_id = 1,
        name = "Back in time",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Back+in+time.mp3"
    )
    song_Tevvez_3 = Song(
        album_id = 1,
        name = "In my dream",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+In+my+dream.mp3"
    )
    song_Tevvez_4 = Song(
        album_id = 1,
        name = "Mystique, Pt. 2",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Mystique%2C+Pt.+2.mp3"
    )
    song_Tevvez_5 = Song(
        album_id = 1,
        name = "Infinity",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Infinity.mp3"
    )
    song_Tevvez_6 = Song(
        album_id = 1,
        name = "Guardian Angel",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Guardian+Angel.mp3"
    )
    song_Tevvez_7 = Song(
        album_id = 1,
        name = "Frozen in time",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Frozen+in+time+(feat.+Mally).mp3"
    )
    song_Tevvez_8 = Song(
        album_id = 1,
        name = "Light",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Light.mp3"
    )
    song_Tevvez_9 = Song(
        album_id = 1,
        name = "Legend",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Legend.mp3"
    )
    song_Tevvez_10 = Song(
        album_id = 1,
        name = "Legacy",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Legacy.mp3"
    )
    song_Tevvez_11 = Song(
        album_id = 1,
        name = "Lost",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Lost.mp3"
    )
    song_Tevvez_12 = Song(
        album_id = 1,
        name = "Oblivion",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Tevvez+-+Oblivion.mp3"
    )

    song_JuiceWRLD_1 = Song(
        album_id = 3,
        name = "Intro",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Intro.mp3"
    )
    song_JuiceWRLD_2 = Song(
        album_id = 3,
        name = "All Girls Are The Same",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+All+Girls+Are+The+Same.mp3"
    )
    song_JuiceWRLD_3 = Song(
        album_id = 3,
        name = "Lucid Dreams",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Lucid+Dreams.mp3"
    )
    song_JuiceWRLD_4 = Song(
        album_id = 3,
        name = "Wasted (feat. Lil Uzi Vert)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Wasted.mp3"
    )
    song_JuiceWRLD_5 = Song(
        album_id = 3,
        name = "Armed And Dangerous",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Armed+And+Dangerous.mp3"
    )
    song_JuiceWRLD_6 = Song(
        album_id = 3,
        name = "Black & White",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Black+%26+White.mp3"
    )
    song_JuiceWRLD_7 = Song(
        album_id = 3,
        name = "Lean Wit Me",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Lean+Wit+Me.mp3"
    )
    song_JuiceWRLD_8 = Song(
        album_id = 3,
        name = "I'll Be Fine",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+I-'ll+Be+Fine.mp3"
    )
    song_JuiceWRLD_9 = Song(
        album_id = 3,
        name = "Used To",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Used+To.mp3"
    )
    song_JuiceWRLD_10 = Song(
        album_id = 3,
        name = "Candles",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Candles.mp3"
    )
    song_JuiceWRLD_11 = Song(
        album_id = 3,
        name = "Scared Of Love (with instrumental by Ghost Loft)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Scared+Of+Love+(with+instrumental+by+Ghost+Loft).mp3"
    )
    song_JuiceWRLD_12 = Song(
        album_id = 3,
        name = "Hurt Me",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Hurt+Me.mp3"
    )
    song_JuiceWRLD_13 = Song(
        album_id = 3,
        name = "I'm Still",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+I-'m+Still.mp3"
    )
    song_JuiceWRLD_14 = Song(
        album_id = 3,
        name = "End Of The Road",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+End+Of+The+Road.mp3"
    )
    song_JuiceWRLD_15 = Song(
        album_id = 3,
        name = "Long Gone",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Juice+Wrld+-+Long+Gone.mp3"
    )

    song_LilUziVert_1 = Song(
        album_id = 2,
        name = "Baby Pluto",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Baby+Pluto.mp3"
    )
    song_LilUziVert_2 = Song(
        album_id = 2,
        name = "Lo Mein",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Lo+Mein.mp3"
    )
    song_LilUziVert_3 = Song(
        album_id = 2,
        name = "Silly Watch",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Silly+Watch.mp3"
    )
    song_LilUziVert_4 = Song(
        album_id = 2,
        name = "POP",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+POP.mp3"
    )
    song_LilUziVert_5 = Song(
        album_id = 2,
        name = "You Better Move",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+You+Better+Move.mp3"
    )
    song_LilUziVert_6 = Song(
        album_id = 2,
        name = "Homecoming",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Homecoming.mp3"
    )
    song_LilUziVert_7 = Song(
        album_id = 2,
        name = "I'm Sorry",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+I-'m+Sorry.mp3"
    )
    song_LilUziVert_8 = Song(
        album_id = 2,
        name = "Celebration Station",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Celebration+Station.mp3"
    )
    song_LilUziVert_9 = Song(
        album_id = 2,
        name = "Bigger Than Life",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Bigger+Than+Life.mp3"
    )
    song_LilUziVert_10 = Song(
        album_id = 2,
        name = "Chrome Heart Tags",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Chrome+Heart+Tags.mp3"
    )
    song_LilUziVert_11 = Song(
        album_id = 2,
        name = "Bust Me",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Bust+Me.mp3"
    )
    song_LilUziVert_12 = Song(
        album_id = 2,
        name = "Prices",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Prices.mp3"
    )
    song_LilUziVert_13 = Song(
        album_id = 2,
        name = " Urgency (feat. Syd)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Urgency+(feat.+Syd).mp3"
    )
    song_LilUziVert_14 = Song(
        album_id = 2,
        name = "Venetia",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Venetia.mp3"
    )
    song_LilUziVert_15 = Song(
        album_id = 2,
        name = "Secure The Bag",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Secure+The+Bag.mp3"
    )
    song_LilUziVert_16 = Song(
        album_id = 2,
        name = "P2",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+P2.mp3"
    )
    song_LilUziVert_17 = Song(
        album_id = 2,
        name = "Futsal Shuffle 2020 - Bonus Track",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Futsal+Shuffle+2020.mp3"
    )
    song_LilUziVert_18 = Song(
        album_id = 2,
        name = "That Way - Bonus Track",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+That+Way.mp3"
    )

    song_DuaLipa_1 = Song(
        album_id = 5,
        name = "Future Nostalgia",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Future+Nostalgia.mp3"
    )
    song_DuaLipa_2 = Song(
        album_id = 5,
        name = "Don't Start Now",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Don-'t+Start+Now.mp3"
    )
    song_DuaLipa_3 = Song(
        album_id = 5,
        name = "Cool",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Cool.mp3"
    )
    song_DuaLipa_4 = Song(
        album_id = 5,
        name = "Physical",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Physical.mp3"
    )
    song_DuaLipa_5 = Song(
        album_id = 5,
        name = "Levitating",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Levitating.mp3"
    )
    song_DuaLipa_6 = Song(
        album_id = 5,
        name = "Pretty Please",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Pretty+Please.mp3"
    )
    song_DuaLipa_7 = Song(
        album_id = 5,
        name = "Hallucinate",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Hallucinate.mp3"
    )
    song_DuaLipa_8 = Song(
        album_id = 5,
        name = "Love Again",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Love+Again.mp3"
    )
    song_DuaLipa_9 = Song(
        album_id = 5,
        name = "Break My Heart",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Break+My+Heart.mp3"
    )
    song_DuaLipa_10 = Song(
        album_id = 5,
        name = "Good In Bed",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Good+In+Bed.mp3"
    )
    song_DuaLipa_11 = Song(
        album_id = 5,
        name = "Boys Will Be Boys",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Dua+Lipa+-+Boys+Will+Be+Boys.mp3"
    )

    song_LilUziVert2_1 = Song(
        album_id = 6,
        name = "Two®",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Two%C2%AE.mp3"
    )
    song_LilUziVert2_2 = Song(
        album_id = 6,
        name = "444+222",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+444%2B222.mp3"
    )
    song_LilUziVert2_3 = Song(
        album_id = 6,
        name = "Sauce It Up",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Sauce+It+Up.mp3"
    )
    song_LilUziVert2_4 = Song(
        album_id = 6,
        name = "No Sleep Leak",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+No+Sleep+Leak.mp3"
    )
    song_LilUziVert2_5 = Song(
        album_id = 6,
        name = "The Way Life Goes (feat. Oh Wonder)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+The+Way+Life+Goes+(feat.+Oh+Wonder).mp3"
    )
    song_LilUziVert2_6 = Song(
        album_id = 6,
        name = "For Real",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+For+Real.mp3"
    )
    song_LilUziVert2_7 = Song(
        album_id = 6,
        name = "Feelings Mutual",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Feelings+Mutual.mp3"
    )
    song_LilUziVert2_8 = Song(
        album_id = 6,
        name = "Neon Guts (feat. Pharrell Williams)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Neon+Guts+(feat.+Pharrell+Williams).mp3"
    )
    song_LilUziVert2_9 = Song(
        album_id = 6,
        name = "Early 20 Rager",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Early+20+Rager.mp3"
    )
    song_LilUziVert2_10 = Song(
        album_id = 6,
        name = "UnFazed (feat. The Weeknd)",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+UnFazed+(feat.+The+Weeknd).mp3"
    )
    song_LilUziVert2_11 = Song(
        album_id = 6,
        name = "Pretty Mami",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Pretty+Mami.mp3"
    )
    song_LilUziVert2_12 = Song(
        album_id = 6,
        name = "How To Talk",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+How+to+Talk.mp3"
    )
    song_LilUziVert2_13 = Song(
        album_id = 6,
        name = "X",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+X.mp3"
    )
    song_LilUziVert2_14 = Song(
        album_id = 6,
        name = "Malfunction",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Malfunction.mp3"
    )
    song_LilUziVert2_15 = Song(
        album_id = 6,
        name = "Dark Queen",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Dark+Queen.mp3"
    )
    song_LilUziVert2_16 = Song(
        album_id = 6,
        name = "XO TOUR Llif3",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+XO+Tour+Llif3.mp3"
    )
    song_LilUziVert2_17 = Song(
        album_id = 6,
        name = "Skir Skirr",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Skir+Skirr.mp3"
    )
    song_LilUziVert2_18 = Song(
        album_id = 6,
        name = "Loaded",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Loaded.mp3"
    )
    song_LilUziVert2_19 = Song(
        album_id = 6,
        name = "Diamonds All On My Wrist",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+Diamonds+All+on+My+Wrist.mp3"
    )
    song_LilUziVert2_20 = Song(
        album_id = 6,
        name = "20 Min",
        song_url = "https://groovify-bucket.s3.us-west-1.amazonaws.com/Lil+Uzi+Vert+-+20+Min.mp3"
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

    db.session.add(song_DuaLipa_1)
    db.session.add(song_DuaLipa_2)
    db.session.add(song_DuaLipa_3)
    db.session.add(song_DuaLipa_4)
    db.session.add(song_DuaLipa_5)
    db.session.add(song_DuaLipa_6)
    db.session.add(song_DuaLipa_7)
    db.session.add(song_DuaLipa_8)
    db.session.add(song_DuaLipa_9)
    db.session.add(song_DuaLipa_10)
    db.session.add(song_DuaLipa_11)

    db.session.add(song_LilUziVert2_1)
    db.session.add(song_LilUziVert2_2)
    db.session.add(song_LilUziVert2_3)
    db.session.add(song_LilUziVert2_4)
    db.session.add(song_LilUziVert2_5)
    db.session.add(song_LilUziVert2_6)
    db.session.add(song_LilUziVert2_7)
    db.session.add(song_LilUziVert2_8)
    db.session.add(song_LilUziVert2_9)
    db.session.add(song_LilUziVert2_10)
    db.session.add(song_LilUziVert2_11)
    db.session.add(song_LilUziVert2_12)
    db.session.add(song_LilUziVert2_13)
    db.session.add(song_LilUziVert2_14)
    db.session.add(song_LilUziVert2_15)
    db.session.add(song_LilUziVert2_16)
    db.session.add(song_LilUziVert2_17)
    db.session.add(song_LilUziVert2_18)
    db.session.add(song_LilUziVert2_19)
    db.session.add(song_LilUziVert2_20)

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
