import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Music(Base):
        __tablename__ = 'songs'
        song_id = Column(String, primary_key=True)
        song_name = Column(String(50))
        artist_name = Column(String(50))
        song_lyrics = Column(Text())

engine = create_engine('sqlite:///lyrics.sqlite')
Base.metadata.create_all(engine)















