from __future__ import annotations

import sys
import threading
import time

class Loading:
    """ Loading class for terasploit console """
    
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor() -> any:
        """ Spinning cursor """
        
        while 1: 
            for cursor in '|/-\\': 
                yield cursor            


    def __init__(self, delay=None, message='') -> None:
        """ Starting point of Loading class """

        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): 
            self.delay = delay
            
        self.message = message


    def spinner_task(self) -> None:
        """ Main function of the class Loading. This prints the spinning cursor along with the message """
        
        count = 0
        msg = self.message
        while self.busy:
            count += 1
            try:
                sys.stdout.write('\b' + f'{msg[:count]}{msg[count].upper()}{msg[count+1:]}' + next(self.spinner_generator) + '\r')
            except IndexError:
                count = 0
                sys.stdout.write('\b' + f'{msg[:count]}{msg[count].upper()}{msg[count+1:]}' + next(self.spinner_generator) + '\r')
                
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()


    def __enter__(self) -> None:
        """ Sets the busy self variable into True and starts a threading on spinner task function """
        
        self.busy = True
        threading.Thread(target=self.spinner_task).start()


    def __exit__(self, exception, value, tb) -> False | None:
        """ Breaks the loop by setting the busy self variable into False """
        
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False