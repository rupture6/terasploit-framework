#######
# Command: Exit
#######

from init.tsf.ui.wildcard import info_print
from init.tsf.core.wildcard import Logger
import time
import logging

class _exit_:
    
    def function():
        current_time = time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')
        Logger('info',f'Console terminated by the user - {current_time}.')
        info_print (f'Console terminated - {current_time}',uplinebreak=True)
        
        raise SystemExit(0)