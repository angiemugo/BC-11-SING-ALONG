import os
import sys


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lyrics.sqlite')
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()

Base = declarative_base()

class Music(Base):
        __tablename__ = 'lyrics'
        song_id = Column(Integer, primary_key=True)
        song_name = Column(String(50))
        artist_id = Column(Integer)
        artist_name = Column(String(50))
        song_lyrics = Column(Text())
        # Base.metadata.create_all(engine)
       #  l1 = lyrics(song_id = "track_id",
       #                     song_name = "track_name",
       #                      artist_id = "artist_id",
       #                      artist_name = "artist_name",
       #                      song_lyrics = "lyrics_id")
       # '''t = lyrics(song_id = "track_id",
       #             song_name = "track_name",
       #              artist_id = "artist_id",
       #              artist_name = "artist_name",
       #              song_lyrics = "lyrics_id")'''
       #  session.add(t)
       #  session.commit()
       #  print












