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

SETBACKS
•	The api only displays the 33% of the total lyrics
•	When a search is done, it only returns the first 10 hits

HOW TO INSTALL
1.	Git  Clone this project at https://github.com/angiemugo/BC-11-SING-ALONG 
2.	Install a virtual environment, preferably virtualenv in this folder and activate it, using  virtualenv env
3.	$ pip install -r requirements.txt
4.	Launch the app by executing app.py and specify the click interactive menu
5.	The class attendance is now up running. The usage commands are well documented, and can be accessed any time by passing the -h or --help option
RESOURCES
•	click
•	SQLalchemy
•	postman




