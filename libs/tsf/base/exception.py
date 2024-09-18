#######
# Base: Exception
#######

import sys; sys.dont_write_bytecode = True
import os

from init.tsf.core.wildcard import Logger
from init.tsf.ui.wildcard import *



class exception_error:
    def __init__(self, line1, line2, line3) -> None:
        self.first   = line1
        self.second  = line2
        self.third   = line3

    def exception_message(self) -> None:
        """ Prints the whole exception message in arranged format """
        
        info_print ('Something went wrong.',type='red',uplinebreak=True)
        info_print (self.first,type='red',downlinebreak=True)

        # Print full traceback.
        count = 0
        for i in self.second:
            count += 1
            type_print (f'({count}) >>>{f.RED}{i}{f.RESET}',speed=15000)

        info_print (self.third,type='red',downlinebreak=True)        
    

class execute:
    """ Execute Shell Command
    
    :params: command -- command from the command line
    :params: parameter -- parameter from the command line
    :params: value -- value from the command line
    
    It will execute the command two times to check the code returned by the 
    command. First execute is suppressed by >/dev/null 2>&1 because it is 
    only for status code checking. If the status code returned is 0, it will 
    proceed on executing the command again with no suppression.
    """

    def __init__(self, command, parameter, value) -> None:
        try:
            self.command = command
            self.parameter = parameter
            self.value = value
            if self.command.lower() == 'exec': # Exec will automatically work, no reason to specify it.
                raise TerasploitUnknownCommand(self.command,'Unknown command was specified in command prompt.')

            self.cmd = f'{command} {parameter} {value}'
            self.check = os.system(f'{self.cmd} >/dev/null 2>&1')
            self.execute_command()
        except KeyboardInterrupt:
            info_print ('Exec interrupted by user.')
            return
        except TerasploitUnknownCommand:
            return


    def execute_command(self) -> None:
        try:
            check_result = True if self.check == 0 else False
            if check_result:
                info_print (f'Exec: {self.command} {self.parameter} {self.value}')
                os.system(self.cmd)
            else:
                raise TerasploitUnknownCommand(self.command,'Unknown command was specified in command prompt.')
        except TerasploitUnknownCommand:
            return


class TerasploitExceptionMessage:
    """ Displays exception message """
    
    def __init__(self,exception_type: str, cause: str) -> None:
        self.cause = cause
        getattr(self,exception_type.lower())()
    
    
    def unknown_command_error(self):
        info_print (f"Unknown command error: '{f.GREEN}{self.cause}{f.RESET}', use '{f.GREEN}help{f.RESET}' to show all commands information.",type='RED')
        
    
    def module_required_error(self):
        info_print (f"Module required error: '{f.GREEN}{self.cause}{f.RESET}', no current module in use.",type='RED')
        

    def payload_required_error(self):
        info_print (f"Payload required error: '{f.GREEN}{self.cause}{f.RESET}', no current payload in use.",type='RED')


    def encoder_required_error(self):
        info_print (f"Encoder required error: '{f.GREEN}{self.cause}{f.RESET}', no current encoder in use.",type='RED')
        
    
    def invalid_option_error(self):
        info_print (f"Invalid option error: '{f.GREEN}{self.cause}{f.RESET}', use command '{f.GREEN}show options{f.RESET}' to display valid options.", type='RED')

        
    def module_exception_error(self):
        info_print (f"Module exception error: '{f.GREEN}{self.cause}{f.RESET}', module ended with an exception.", type='RED')
        
    
    def start_session_error(self):
        info_print (f"Start session error: '{f.GREEN}{self.cause}{f.RESET}', non-exploit module has attempted to start a session.", type='RED')
        
        
    def module_error(self):
        info_print (f"Module error: '{f.GREEN}{self.cause}{f.RESET}', failed to import! invalid module.",type='RED')
        
        
    def value_error(self):
        info_print (f"Value error: '{f.GREEN}{self.cause}{f.RESET}', no value was specified.", type="RED")
       
        
    def param_error(self):
        info_print (f"Parameter error: '{f.GREEN}{self.cause}{f.RESET}', no parameter was specified.", type="RED")
        

class TerasploitException(Exception):
    """ Terasploit Base Exception Handler """
    
    def __init__(self,cause: str, exception_type: str, message: str = "") -> None:
        Logger('error',"Terasploit Exception!")
        if message:
            Logger('error',f"Exception Message: {message}")
        Logger('error',f"Exception Cause: {cause}")
        TerasploitExceptionMessage(exception_type,cause)
        super(TerasploitException,self).__init__(message)
        
        
class TerasploitUnknownCommand(TerasploitException):
    """ Raised when unknown command was specified """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"unknown_command_error",exception_message)


class TerasploitModuleError(TerasploitException):
    """ Raised when an unknown module was imported """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"module_error",exception_message)


class TerasploitValueError(TerasploitException):
    """ Raised when no value was specified from command """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"value_error",exception_message)
        

class TerasploitParamError(TerasploitException):
    """ Raised when no parameter was specified from command """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"param_error",exception_message)
        

class TerasploitModuleRequired(TerasploitException):
    """ Raised when a function was triggered that requires module but no current module """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"module_required_error",exception_message)
        

class TerasploitPayloadRequired(TerasploitException):
    """ Raised when a function was triggered that requires payload but no current module """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"payload_required_error",exception_message)
        

class TerasploitEncoderRequired(TerasploitException):
    """ Raised when a function was triggered that requires encoder but no current module """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"encoder_required_error",exception_message)
        

class TerasploitInvalidOption(TerasploitException):
    """ Raised when an unknown option parameter was specified """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"invalid_option_error",exception_message)
        

class TerasploitModuleException(TerasploitException):
    """ Raised when a module ended with exception """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"module_exception_error",exception_message)
        
        
class TerasploitStartSessionError(TerasploitException):
    """ Raised when a non-exploit module started a session """
    
    def __init__(self, exception_cause: str, exception_message: str):
        super().__init__(exception_cause,"start_session_error",exception_message)