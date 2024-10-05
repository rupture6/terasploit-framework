#######
# Core: Contents Container
#######

from libs.tsf.core.console.module_container import (
    set_encoder,
    set_payload,
    set_module,
)

from libs.tsf.core.console.variable_container import (
    set_command_name,
    set_command_parameter,
    set_args_value,
    set_parameter_value,
    set_prompt,
    set_user
)

class Global:
    """ Global - Contains all the global variables of the console """

    # Non-static Variables :: Changeable
    
    User       =  set_user('tsf')
    Prompt     =  set_prompt('>')
    
    Command    =  set_command_name(None)
    Parameter  =  set_command_parameter(None)
    Value      =  set_parameter_value(None)
    Args       =  set_args_value(None)

    Module     =  set_module(None,None)
    Payload    =  set_payload(None,None)
    Encoder    =  set_encoder(None,None)
    
    # Static Variable :: Non-changeable
    
    GlobalVariables = ['payload','encoder','user','prompt']