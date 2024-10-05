#######
# Interpreter: Core
#######

from init.teralib.core import (
    Get,
    Global,
    Logger
)
from init.teralib.base import (
    execute,
    check_missing_opt,
)
from init.teralib.ui import print_info
from init.framework import (
    exploit_session,
    Exit,
    Search,
    Use,
    Back,
    Banner,
    Show,
    Set,
    Unset,
    Help,
    Info
)

@check_missing_opt
def module_commands(command) -> None:
    """ Executes module attribute """
    
    try:
        if command.lower() == 'exploit':
            if hasattr(Get.module()[0],command.lower()):
                exploit_session()
                return
                
        getattr(Get.module()[0],command.lower())()
                
    except KeyboardInterrupt:
        print ("Module Interrupt: module function was interrupted by user.")
        return
        
    except Exception as error:
        print_info (error,type='RED')
        return
        

class commands(object):
    """ Framework commands -- command call function class """
    
    def EXIT(self) -> None:
        # Terminates the framework console
        Exit._exit_.function()
    
    
    def SEARCH(self) -> None:
        # Searches for a module path by str matching
        Search._search_.function()
        
        
    def USE(self) -> None:
        # Imports the module from its path to allow module interaction
        Use._use_.function()
        
        
    def BACK(self) -> None:
        # Removes current module in use and clears info and opt containers
        Back._back_.function()
        
        
    def BANNER(self) -> None:
        # Re-displays the console banner (not a useless command, its cool)
        Banner._banner_.function()
        
        
    def SHOW(self) -> None:
        # Displays information/contents on a certain specified parameter
        Show._show_.function()
        
        
    def SET(self) -> None:
        # Inserts a value from a module option or global option
        Set._set_.function()
        
        
    def UNSET(self) -> None:
        # Removes a value from a module option or global option
        Unset._unset_.function()
        
        
    def HELP(self) -> None:
        # Displays commands informations
        Help._help_.function()
        
        
    def INFO(self) -> None:
        # Displays full module information
        Info._info_.function()
    
    
    def OPTIONS(self) -> None:
        # Shortcut command for displaying module options
        Show._show_.module_opt()

        
class command_function(commands):
    """ Command function handler """
    
    def execute(self,command,parameter,value,args) -> None:
        if command in ['run','exploit']:
            module_commands(command)
            return

        if hasattr(self,f"{command.upper()}"):
            command_function = getattr(self,f"{command.upper()}")
            
            for container, val in zip(['Command','Parameter','Value','Args'],[command,parameter,value,args]):
                setattr(Global,container,val)
            
            Logger('info',f"command:[{command}], parameter:[{parameter}], value:[{value}], opt:[{args}]")
            command_function()
            return
        
        else:
            Logger('info',f"'-exec- command:[{command}], parameter:[{parameter}], value:[{value}]")
            execute(command,parameter,value)
            return