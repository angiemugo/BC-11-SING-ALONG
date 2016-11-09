import click
import json
import requests
from prettytable import PrettyTable as table
from db import Music
from sqlalchemy import create_engine

engine = create_engine('sqlite:///lyrics.sqlite')
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Lyrics:

    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key = "d80da5faf57de840510a37c527f2cb51"

    def song_find(self, query):
        method = "track.search"
        query_string = {"apikey": self.api_key, "q": query}
        response = requests.get(self.api + method, params=query_string)
        data = response.json()
        t = table(['Track ID', 'Track Name', 'Artist Name', 'lyrics_id'])
        for item in data['message']['body']['track_list']:  # [0]['track']['artist_name']
            song_id = item['track']['track_id']
            song_name = item['track']['track_name']
            artist_id = item['track']['artist_id']
            artist_name = item['track']['artist_name']
            lyrics_id = item['track']['lyrics_id']
            t.add_row([song_id, song_name, artist_name, lyrics_id])
        print t

        # Get song lyrics

    def song_view(self, track_id):
        track_id = raw_input("Enter track_id of song to view its lyrics")
        #if self.check_database(track_id)is None:
        method = "track.lyrics.get"
        query_string = {"apikey": self.api_key, "track_id": track_id}
        response = requests.get(self.api + method, params=query_string)
        data = response.json()
        print data["message"]["body"]["lyrics"]["lyrics_body"]
        #if "lyrics_id" is None:
            #print "sorry, lyrics for above song not found"

        '''def check_database(self, track_id):
            lyric.check_database(track_id)

            return False'''
        def song_save(self, track_id):

            track_id = raw_input("enter treack_id")
                #if not self.check_database(track_id):
            method = "track.get"
            query_string = {"apikey": self.api_key, "track_id": track_id}
            response = requests.get(self.api + method, params=query_string)
            #print(self.api + method)
            data = response.json()
            # print data["message"]["body"]["lyrics"]["lyrics_body"]
            session = Session()
            music = Music()
            music.song_id = track_id
            music.song_name = data["message"]["body"]["track"]["track_name"]
            music.artist_name = data["message"]["body"]["track"]["artist_name"]
            # get lyrics from lyrics.get
            method = "track.lyrics.get"
            query_string = {"apikey": self.api_key, "track_id": track_id}
            response = requests.get(self.api + method, params=query_string)
            data = response.json()
            music.song_lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]

            session.add(music)
            session.commit()

            #if not self.check_database(track_id):




        #def song_clear(self):






if __name__ == "__main__":
    lyric = Lyrics()
    while True:
        print "\nWhat would you like to do?"
        print "*" * 30
        print "1: Find a song"
        print "2: View Song Lyrics"
        print "3: Save Song Locally"
        print "4: Clear Database"
        print "5: To Exit"
        print "*" * 30
        menu_item = raw_input("Please enter your selection: ")
        if menu_item == "1":
            query = raw_input("Enter text to search for song, lyrics or artist: ")
            lyric.song_find(query)



        elif menu_item == "2":
            lyric.song_view("track_id")


        elif menu_item == "3":

            lyric.song_save("track_id")




        elif menu_item == "4":
            lyric.song_clear()
            pass

        elif menu_item == "5":
            print "Goodbye"
            exit(0)

        else:
            print "Invalid Entry"








