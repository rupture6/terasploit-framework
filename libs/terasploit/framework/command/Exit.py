#######
# Command: Exit
#######

import time
from init.teralib.core import Logger
from init.teralib.ui import print_info

# Command class

class _exit_:
    
    @staticmethod
    def function():
        current_time = time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')
        
        Logger('info',f'Console terminated by the user - {current_time}.')
        print_info(f'Console terminated - {current_time}')
        
        raise SystemExit(0)