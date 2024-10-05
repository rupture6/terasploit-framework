#######
# Interpreter: Base
#######

import sys
import time
import traceback

from libs.terasploit.framework.interpreter.core import command_function
from libs.terasploit.framework.formatter.command_parse import parse_command
from libs.tsf.ui.prompt import prompt
from init.teralib.core import (
    History,
    Global,
    Logger
)
from init.teralib.base import (
    exception_error,
    TerasploitException
)


class interpreter:

    def __init__(self) -> None:
        """ Startup of the interpreter """
        
        History.access()
        Logger('info',f"Console started! - {time.strftime('%Z %H:%M:%S - %A, %B %e, %Y')}.")
        interpreter.command_prompt()
        
        
    @staticmethod
    def prompt_content() -> tuple[str,str,str]:
        """ Prompt contents """
        
        user = getattr(Global,'User')
        _, path = getattr(Global,'Module')
        prompt = getattr(Global,'Prompt')

        return user, prompt, path
 
 
    @staticmethod
    def command_prompt():
        """ The command line of the console, this is where all the commands are gathered """
        
        while True:
            try:
                command, parameter, value, args = parse_command(input(prompt(interpreter.prompt_content())))
                if not command:
                    continue
                
                command_function().execute(command, parameter, value, args)

            except TerasploitException:
                continue
            
            except KeyboardInterrupt:
                print ("Keyboard Interrupt: use the command 'exit' to terminate the program.")
                continue

            except Exception as error:
                lines = traceback.format_exc().splitlines()
                trace = traceback.format_tb(sys.exception().__traceback__)
                exception_error(lines[0], trace, lines[-1]).exception_message()
                Logger('error',error)
                continue