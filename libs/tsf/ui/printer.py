#######
# UI: Printer
#######

import sys
import time
import os

from libs.tsf.ui.termcolor import tb
from libs.tsf.ui.termline import line_feed


def info_print(content,type='BLUE',uplinebreak=False,downlinebreak=False,end=line_feed()) -> None:
    """ Prints text with text templates [*] [+] [-] [!] """
    
    template_type = getattr(tb,type.upper())
    template = f'{template_type} {str(content)}'
    
    dictionary = {
        'TRUE_TRUE'   :  f"{line_feed()}{template}{line_feed()}",
        'TRUE_FALSE'  :  f"{line_feed()}{template}",
        'FALSE_TRUE'  :  f"{template}{line_feed()}",
        'FALSE_FALSE' :  f"{template}"
    }
    
    key = f"{str(uplinebreak).upper()}_{str(downlinebreak).upper()}"
    print (dictionary[key],end=end)

        
def type_print(content,speed: int = 100):
    """ Creates a type writer effect when printing text """
    
    for chars in content + '\n':
        sys.stdout.write(chars)
        sys.stdout.flush()
        time.sleep(10./speed)
        
        
def print_overlap(content,count):
    """ Prints text that overlaps from the terminal length on description level """
    
    tl = os.get_terminal_size()[0]
    con = content[tl:]
    while True:
        print (f"{' '*count}{con[:tl].lstrip(' ')}")
        if con[tl:]:
            con = con[tl:]
        else:
            break