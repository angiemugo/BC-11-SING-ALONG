"""
    Commands:
        song_find <query>
        song_view <track_number>
        song_save <track_id>
        clear
        quit
    Options:
        -h, --help  Show this screen and exit

"""


from docopt import docopt, DocoptExit
import cmd
import os
from singalong import Lyrics

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

lyric = Lyrics()
class Singalong (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_song_find(self, arg):
        """Usage: song_find <query>"""
        query = arg['<query>']
        # lyric = Lyrics()
        song_table = lyric.song_find(query)
        print song_table


    @docopt_cmd
    def do_song_view(self, arg):
        """Usage: song_view <track_number>"""
        song_id = arg['<track_number>']
        # lyric = Lyrics()
        lyric.song_view(song_id)

    @docopt_cmd
    def do_song_save(self, arg):
        """Usage: song_save <track_id>"""
        song_id = arg['<track_id>']
        lyric.song_save(song_id)

    @docopt_cmd
    def do_song_clear(self, arg):
        """Usage: clear """
        # lyric = Lyrics()
        lyric.song_clear()



    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        print("Exiting...")
        exit()

if __name__ == "__main__":
    try:
        Singalong().cmdloop()
    except KeyboardInterrupt:
        print('Exiting application')