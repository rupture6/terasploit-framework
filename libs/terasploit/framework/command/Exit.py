#######
# Command: Exit
#######

from init.tsf.ui.wildcard import info_print
import time
import logging

class _exit_:
    
    def function():
        current_time = time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')
        logger = logging.getLogger()
        logger.info(f'Console terminated by the user - {current_time}.')
        info_print ('Console terminated - ' + current_time,uplinebreak=True)
        
        raise SystemExit(0)