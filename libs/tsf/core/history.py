#######
# Core: History
#######

import readline
import atexit
import os

class History:
    """ Command History Class 
    
    Creates/access command history file to be used on user input to reuse
    old command inputs by using arrow keys. This will allow the user input
    to act like a gnu terminal.
    """

    def access() -> None:
        history_file = os.path.join(os.path.expanduser("~"), ".terasploit_console_history")

        history_length = 1000
        if not os.path.exists(history_file):
            with open(history_file, 'a+') as file:
                file.close()

        readline.read_history_file(history_file)
        readline.set_history_length(history_length)
        atexit.register(readline.write_history_file, history_file)