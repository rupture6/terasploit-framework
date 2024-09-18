#######
# Core: Contents Container
#######

from init.tsf.core.console.wildcard import *

class Global:
    """ Global - Contains all the global variables of the console """

    # Non-static Variables :: Changeable
    
    User = set_user('tsf')
    Prompt = set_prompt('>')
    
    Command = set_command_name(None)
    Parameter = set_command_parameter(None)
    Value = set_parameter_value(None)
    Options = set_options_value(None)

    Module = set_module(None,None)
    Payload = set_payload(None,None)
    Encoder = set_encoder(None,None)
    
    DefaultPayload = set_module_default_payload(None)
    
    
    # Static Variable :: Non-changeable
    
    GlobalVariables = ['payload','encoder','user','prompt']