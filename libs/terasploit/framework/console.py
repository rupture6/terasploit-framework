from __future__ import annotations

import sys
import threading
import time

from init.tsf.core.wildcard import *
from init.tsf.ui.wildcard import *
from init.tsf.base.wildcard import *

from libs.terasploit.framework.interpreter import base


class Loading:
    """ Loading function for terasploit console
    
    This function displays a loading spinner while a 
    process is on going.
    """
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor() -> any:
        """ Spinning cursor """
        
        while 1: 
            for cursor in '|/-\\': 
                yield cursor            


    def __init__(self, delay=None, message='') -> None:
        """ Starting point of Loading class.
        
        This set the spinner generator to spinning cursor
        to be used on spinner task.
        """

        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): 
            self.delay = delay
            
        self.message = message


    def spinner_task(self) -> None:
        """ Spinner task function.
        
        This will be the main function of the class Loading.
        This prints the spinning cursor along with the message.
        """
        
        count = 0
        msg = self.message
        while self.busy:
            count += 1
            sys.stdout.write('\b' + f'{msg[:count]}{msg[count].upper()}{msg[count+1:]}' + next(self.spinner_generator) + '\r')
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()


    def __enter__(self) -> None:
        """ __enter__
        
        Sets the busy self variable to true and starts
        a threading on spinner task function.
        """
        
        self.busy = True
        threading.Thread(target=self.spinner_task).start()


    def __exit__(self, exception, value, tb) -> False | None:
        """ __exit__
        
        This breaks the loop by setting the busy self variable
        into False, hence stopping the whole function. 
        
        It will also check for exception. If error is detected, 
        it will return False.
        """
        
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


# log & console startup
class start(Logs):
    def __init__(self):
        """ :Start:
        
        Gathers all the modules to be counted in console banner then
        start the logs by calling it. Lastly, it will start the
        console by calling its function.
        
        Exception here are still required despite already having an
        exception at terasploit starter. This is because it's calling
        a function with no exception from a class, therefore it's not
        covered by the exception of the starter file.
        
        Some tsf libraries doesn't have an exception. It straightly does
        its job once called, but they're made to not fail, the only thing
        that will make tsf libraries fail with its function is when the
        user used keyboard interrupt.
        """
        
        try:
            self.logs()
            modules = Search.all_modules()
            banner(modules)
            base.interpreter()
            
        except KeyboardInterrupt:
            clean_last_line()
            print ('[*] Terminated via keyboard interrupt...')
            raise SystemExit(130)
    
        except Exception as error:
            clean_last_line()
            print (f'[*] Startup failed...')
            print (f'[*] Error: {error}')
            raise SystemExit(1)