# bc-11-sing-along
DESCRIPTION
sing-along app is an application built on python that enables a user to find lyrics using either lyrics, song name or artist name. 
it is a command line application based on click.
DEPENDENCIES
Backend dependencies for this application are api,sqlalchemy orm and click.
FUNCTIONS
This app has four functionalities:song_save, song_view, song_search and clear.
•	song search,searches for song details(song id,song name, artist name, has lyrics)
•	Song_view- the song id is used to view the song lyrics. The song_id is provided by the song_search
•	Song-save- sqlalchemy is used to create the database models while sqlite is used to interact with the data.
•	Clear- an sqlalchemy command is used to clear database

Setbacks
•	The api only displays the 33% of the total lyrics
•	When a search is done, it only returns the first 10 hits


