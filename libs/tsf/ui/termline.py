#######
# UI: Termline
#######

import sys


def line_break() -> None:
    """ Prints none to create a line break """
    
    print () # -- line break --
        

def clean_last_line() -> None:
    """ Cleans the current line from the terminal """

    sys.stdout.write('\r'+' '*80+'\r')
    sys.stdout.flush()

    
def up_cursor_delete() -> None:
    """ Up cursor then delete line """
    
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()
    

def carriage_return() -> str:
    """ Returns str 'carriage return' escape char """
    
    return '\r'


def line_feed() -> str:
    """ Returns str 'line feed' escape char """
    
    return '\n'