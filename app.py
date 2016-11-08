import cmd
import json
import requests
from prettytable import PrettyTable as table


class Lyrics:
    def __init__(self):
        self.api = "http://api.musixmatch.com/ws/1.1/"
        self.api_key="d80da5faf57de840510a37c527f2cb51"

    def song_find(self,query):
        method= "track.search"
        query_string={"apikey":self.api_key , "q":query}
        response=requests.get(self.api + method,params=query_string)
        data=response.json()
        t = table(['Track ID', 'Track Name', 'Artist Name'])
        for item in data['message']['body']['track_list']:  # [0]['track']['artist_name']
            song_id = item['track']['track_id']
            song_name = item['track']['track_name']
            artist_id = item['track']['artist_id']
            artist_name = item['track']['artist_name']
            lyrics_id = item['track']['lyrics_id']
            t.add_row([song_id,song_name,artist_name])
        print t

    def song_view(self, track_id):
        if not self.check_database(song_id):
            method = "track.lyrics.get"
            query_string={"apikey":self.api_key, "track_id":track_id}
            response = requests.get(self.api+method,params=query_string)
            data=response.json()
            print data["message"]["body"]["lyrics"]["lyrics_body"]

    def song_save(self):
        pass

    def song_clear(self):
        pass

    def check_database(self, song_id):
        #implement dbquery here
        #if song_id not in database:
        return False


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
            song_id=raw_input("Enter song ID")
            lyric.song_view(song_id)

        elif menu_item=="3":
            lyric.song_save()
            pass

        elif menu_item=="4":
            lyric.song_clear()

        elif menu_item=="5":
            print "Goodbye"
            exit(0)

        else:
            print "Invalid Entry"








