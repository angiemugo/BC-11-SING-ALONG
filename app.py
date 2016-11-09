import requests
from prettytable import PrettyTable as table

from sqlalchemy import create_engine

engine = create_engine('sqlite:///lyrics.sqlite')
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from db import Music

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Lyrics():
    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key="d80da5faf57de840510a37c527f2cb51"
        self.songs={}
        self.session = Session()

    def song_find(self,query):

        method = "track.search"
        query_string = {"apikey": self.api_key, "q": query}
        data = requests.get(self.api + method, params=query_string).json()
        t = table(['Track Number','Track ID', 'Track Name', 'Artist Name','Has Lyrics'])
        index=1
        for item in data['message']['body']['track_list']:  # [0]['track']['artist_name']
            track_id = item['track']['track_id']
            track_name = item['track']['track_name']
            artist_name = item['track']['artist_name']
            has_lyrics = item['track']['has_lyrics']
            song = {}
            song["id"]=track_id
            song["name"]=track_name
            song["artist_name"]=artist_name
            if has_lyrics=="0":
                song["lyrics"]="NO"
            else:
                song["lyrics"]="YES"
            t.add_row([index,track_id,track_name,artist_name,song["lyrics"]])
            self.songs[index]=song
            index+=1
        print t
        self.song_view()



    def song_view(self):
        track_number=raw_input("\nSelect song by track number: ")
        track= self.songs[int(track_number)]
        track_id = str(track["id"])
        if self.session.query(Music, Music.song_id == track_id).count() == 0:
            method = "track.lyrics.get"
            query_string = {"apikey": self.api_key, "track_id": track_id}
            response = requests.get(self.api + method, params=query_string)
            data = response.json()
            print "\n\n"+track["name"] + " by " + track["artist_name"]
            print "-"*50
            #print data
            lyrics=data["message"]["body"]["lyrics"]["lyrics_body"]
            track["lyrics"]=lyrics
            print lyrics
            self.songs[track_id]=track
            self.song_save(track_id)
        else:
            for row in self.session.query(Music, Music.song_id == track_id):
                print "\n\n" + row.Music.song_name + " by " + row.Music.artist_name
                print "-" * 50
                print row.Music.song_lyrics
                print "\n\n"




    def song_save(self,track_id):
        track=self.songs[track_id]
        music=Music()
        music.song_id=track["id"]
        music.artist_name=track["artist_name"]
        music.song_lyrics=track["lyrics"]
        music.song_name=track["name"]
        self.session.add(music)
        self.session.commit()


    def song_clear(self):
        s=self.session.query(Music).delete()
        self.session.commit()
        print "**************Database Cleared**************\n\n"




if __name__ == "__main__":
    lyric=Lyrics()
    while True:
        print "\nWhat would you like to do?"
        print "*"*30
        print "1: Find a song"
        print "2: View Song Lyrics"
        print "3: Save Song Locally"
        print "4: Clear Databse"
        print "5: To Exit"
        print "*" * 30
        menu_item=raw_input("Please enter your selection: ")

        if menu_item=="1":
            query=raw_input("Enter text to search for song, lyrics or artist: ")
            lyric.song_find(query)

        elif menu_item=="2":
            lyric.song_view()

        elif menu_item=="3":
            lyric.song_save()

        elif menu_item=="4":
            lyric.song_clear()

        elif menu_item=="5":
            print "Goodbye"
            exit(0)

        else:
            print "Invalid Entry"