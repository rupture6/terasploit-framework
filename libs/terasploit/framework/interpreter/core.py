#######
# Interpreter: Core
#######

from init.tsf.core.wildcard import Get, Global, Logger

from init.tsf.base.wildcard import (
    TerasploitStartSessionError, 
    TerasploitModuleException, 
    TerasploitUnknownCommand, 
    execute
)

from init.tsf.ui.wildcard import info_print
from init.terasploit.framework.command.wildcard import *

from libs.terasploit.framework.exploit.handler import exploit_session
from libs.terasploit.framework.command.util.decorator import check_missing_opt


class module_return_handler:
    """ Handles the module return """
    
    def __init__(self, module_return: str, boolean: bool) -> None:
        module_type = Get.module()[0].module_type.lower()
        module = f"{module_type[0].upper()}{module_type[1:]}"
        
        if module_return == 'session':
            if module_type != 'exploit':
                raise TerasploitStartSessionError(module,'a non-exploit module has attempted to start a session')
            Logger('info','Exploit module has started a session')
            exploit_session(start_session=boolean)
            
        if module_return == 'done':
            if boolean == True:
                info_print (f'{module} module done running!')
                Logger('info','Module done running!')
            if boolean == False:
                Logger('info','Module done running, message was suppressed.')
        
        if module_return == 'exception':
            if boolean == True:
                raise TerasploitModuleException(module,'Module ended with an exception error')
            if boolean == False:
                Logger('info','Module ended with an exception error, exception was suppressed.')
                info_print (f'{module} module done running!')


class module_commands:
    """ Executes commands from module """
    
    @check_missing_opt
    def execute(command) -> None:
        try:
            module_return, boolean = getattr(Get.module()[0],command.lower())()
            if not module_return:
                return
            
            module_return_handler(module_return.lower(),boolean)
        except KeyboardInterrupt:
            print ("Module Interrupt: module function was interrupted by user.")
            return
        except AttributeError as error:
            info_print (error,type='RED')
            raise TerasploitUnknownCommand(command,'Unknown module command was specified.')


class commands(object):
    def EXIT(self) -> None:
        """ Terminates the framework console """
        
        Exit._exit_.function()
    
    def SEARCH(self) -> None:
        """ Searches for a module path by str matching """
        
        Search._search_.function()
        
    def USE(self) -> None:
        """ Imports the module from its path to allow module interaction """
        
        Use._use_.function()
        
    def BACK(self) -> None:
        """ Removes current module in use and clears info and opt containers """
        
        Back._back_.function()
        
    def BANNER(self) -> None:
        """ Re-displays the console banner (not a useless command, its cool) """
        
        Banner._banner_.function()
        
    def SHOW(self) -> None:
        """ Displays information/contents on a certain specified parameter """
        
        Show._show_.function()
        
    def SET(self) -> None:
        """ Inserts a value from a module option or global option """
        
        Set._set_.function()
        
    def UNSET(self) -> None:
        """ Removes a value from a module option or global option """
        
        Unset._unset_.function()
        
    def HELP(self) -> None:
        """ Displays commands informations """
        
        Help._help_.function()
        
    def INFO(self) -> None:
        """ Displays full module information """
        
        Info._info_.function()
    
    def OPTIONS(self) -> None:
        """ Shortcut command for displaying module options """
        
        Show._show_.module_opt()

        
class function_handler(commands):
    """ Command function handler """
    
    def __init__(self,command,parameter,value,options) -> None:
        self.command = command
        self.parameter = parameter
        self.value = value
        self.options = options
        
        
    def execute_command(self) -> None:
        command, parameter, value, opt = self.command, self.parameter, self.value, self.options
        
        module_command = ['run','exploit']
        if command in module_command:
            if command == 'run' or command == 'exploit':
                Logger('info','Module executed!')
                
            module_commands.execute(command)
            return

        if hasattr(self,f"{command.upper()}"):
            command_function = getattr(self,f"{command.upper()}")

            # Setting command line values to global variables via class descriptors
            setattr(Global,'Command',command)
            setattr(Global,'Parameter',parameter)
            setattr(Global,'Value',value)
            setattr(Global,'Options',opt)
            
            Logger('info',f"'{getattr(Global,'User')}' :prompt: command: ({command}), parameter: ({parameter}) value: ({value}) opt: ({opt})")
            command_function()
            return
        
        else:
            Logger('info',f"'{getattr(Global,'User')}' :prompt: exec command:({command}), parameter:({parameter}), value:({value})")
            execute(command,parameter,value)
            return