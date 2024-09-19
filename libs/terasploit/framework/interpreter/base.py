#######
# Interpreter: Base
#######

import sys
import time
import traceback

from init.tsf.ui.wildcard import prompt
from init.tsf.core.wildcard import History, Global, Logger
from init.tsf.base.wildcard import TerasploitException, exception_error
from init.terasploit.framework.formatter.wildcard import command_line
from libs.terasploit.framework.interpreter.core import function_handler


class interpreter:
    def __init__(self) -> None:
        History.access()
        current_time = time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')
        Logger('info',f'Console started! - {current_time}.')
        self.command_prompt()
        
        
    def prompt_content(self) -> tuple[str,str,str]:
        """ Prompt contents - Grabs user, path and prompt char from contents container """
        
        user = getattr(Global,'User')
        _, path = getattr(Global,'Module')
        prompt = getattr(Global,'Prompt')

        return user, prompt, path
 
 
    def command_prompt(self):
        """ Command prompt - Gathers command line from the user and pass it to the function handler """
        
        while True:
            try:
                command, parameter, value, opts = command_line.parse(input(prompt.generate_template(self.prompt_content())))
                if not command:
                    continue

                function_handler(command, parameter, value, opts).execute_command()                
                
            except KeyboardInterrupt:
                print ("Keyboard Interrupt: use the command 'exit' to terminate the program.")
                continue
            
            except TerasploitException:
                continue

            except Exception as error:
                lines = traceback.format_exc().splitlines()
                trace = traceback.format_tb(sys.exception().__traceback__)
                exception_error(lines[0], trace, lines[-1]).exception_message()
                Logger('error',error)
                continue