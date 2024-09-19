#######
# Command/Util: Decorator 
#######

from __future__ import annotations

from init.tsf.base.wildcard import (
    TerasploitModuleRequired,
    TerasploitUnknownCommand,
    TerasploitEncoderRequired,
    TerasploitPayloadRequired,
    TerasploitParamError,
    TerasploitValueError
)

from init.tsf.core.wildcard import Get, Set
from init.tsf.ui.wildcard import line_break, info_print
from init.tsf.util.wildcard import usage_banner

from libs.terasploit.framework.opts.opt_distributor import Opt



def check_missing_opt(function) -> any:
    """ checks if there is any required options that has no value """
    
    def wrapper(command) -> any|None:
        if command not in ['run','exploit']: # checks if the module command is for module execution
            pass
        
        module = Get.module()[0]
        if not module:
            raise TerasploitModuleRequired(command,'Attempted to execute a module with no current module in use.')
        else:
            if not hasattr(module,command.lower()):
                raise TerasploitUnknownCommand(command,'Unknown module command was specified.')
            
        not_available = 0
        for available, module in [Opt('auxiliary').Get(),Opt('encoder').Get(),Opt('exploit').Get(),Opt('payload').Get()]:
            if not available:
                continue
            
            opt_name = [x for x in Opt(module).Get()[0]]
            for i in opt_name:
                name_content = [x for x in [x for x in Opt(module).Get()[0][i][0]]][0]
                required = [x for x in [x for x in Opt(module).Get()[0][i][0]]][1]
                if not name_content:
                    if required == 'yes':
                        not_available += 1
                        print (f'missing value => {i}')
                    else:
                        continue
                        
        if not_available != 0:
            return
        
        return function(command)
    return wrapper


def module_required(function) -> any|None:
    """ check if there's current module in use """
    
    def wrapper() -> any|None:
        module, _ = Get.module()
        command = Get.command()

        if not module:
            raise TerasploitModuleRequired(command,"Module is required to execute the function.")
        
        return function()
    return wrapper


def payload_required(function) -> any|None:
    """ check if there's current payload in use """
    
    def wrapper() -> any|None:
        payload, _ = Get.payload()
        command = Get.command()
        if not payload:
            raise TerasploitPayloadRequired(command,"Payload is required to execute the function.")
        
        return function()
    return wrapper


def encoder_required(function) -> any|None:
    """ check if there's current payload in use """
    
    def wrapper() -> any|None:
        encoder, _ = Get.encoder()
        command = Get.command()
        if not encoder:
            raise TerasploitEncoderRequired(command,"Encoder is required to execute the function.")
        
        return function()
    return wrapper


def show_usage(function) -> any|None:
    """ checks if a parameter was specified by the command line | used by value_required decorator """
    
    def wrapper() -> any|None:
        module, _ = Get.module()
        command = Get.command()
        parameter = Get.parameter()
        
        if not parameter:
            command_with_usage_banner: list = ['show','set','search','info','use','unset']
            if command.lower() in command_with_usage_banner:
                if parameter in command_with_usage_banner:
                    get = getattr(usage_banner,f'{parameter}_usage')
                else:
                    get = getattr(usage_banner,f'{command}_usage')
                    
                banner = get()
                for key, value in banner.items():
                    if 'Usage' in key:
                        print (key)
                    else:
                        line_break()
                        print (key)
                    for val in value:
                        print (val)
                line_break()

            if command.lower() == 'info':
                if module:
                    pass
                
        return function()
    return wrapper


def param_required(function) -> any:
    """ Check the existence of parameter from the command line """
    
    @show_usage
    def wrapper() -> any|None:
        command = Get.command()
        param = Get.parameter()
        
        if not param:
            raise TerasploitParamError(command,"No command parameter was specified.")
        
        return function()
    return wrapper


def value_required(function) -> any:
    """ Check the existence of value from the command line """
    
    @show_usage
    def wrapper() -> any|None:
        command = Get.command()
        value = Get.parameter() if command.lower() in ['use','info','search'] else Get.value()
    
        if not value:
            raise TerasploitValueError(command,"No command value was specified.")

        return function()
    return wrapper
            

def module_insert_payload(function) -> any:
    """ Inserts the imported payload inside the module class variable payload """

    def wrapper() -> any|None:
        current_payload, current_payload_path = Get.payload()
        module, _ = Get.module()
        
        if current_payload != None:
            if not hasattr(module,'payload'):
                return
            
            default_payload_path = module.payload
            Set.defaultpayload(default_payload_path)
            
            setattr(module,'payload',current_payload)
            info_print(f"Using current payload {current_payload_path.replace('modules/','')}")

            return
        return function()
    return wrapper


def module_insert_encoder(function) -> any:
    """ Inserts the imported encoder inside the module class variable encoder """
    
    def wrapper() -> any|None:
        encoder, _ = Get.encoder()
        module, _ = Get.module()
        
        if encoder != None:
            if not hasattr(module,'encoder'):
                return

            setattr(module,'encoder',encoder)

            return
        return function()
    return wrapper