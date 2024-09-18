#######
# Core: Contents Dispatcher
#######

from libs.tsf.core.contents_container import Global

class Get:
    """ Get - Access a value from global handler and return it to the functions that required it """
    
    def command() -> str:
        return Global.Command

    def parameter() -> str:
        return Global.Parameter

    def value() -> str:
        return Global.Value
    
    def options() -> str:
        return Global.Options
    
    def user() -> str:
        return Global.User
    
    def prompt() -> str:
        return Global.Prompt
    
    def globalvariables() -> list:
        return Global.GlobalVariables
    
    def module() -> tuple[any,any]: 
        module, path = Global.Module
        return module, path
    
    def payload() -> tuple[any,any]:
        payload, path = Global.Payload
        return payload, path
    
    def defaultpayload() -> str:
        default = Global.DefaultPayload
        return default
    
    def encoder() -> tuple[any,any]:
        encoder, path = Global.Encoder
        return encoder, path
    
class Set:
    """ Set - Changes values from non-static variables of global handler """
    
    def command(value):
        setattr (Global,'Command',value)
    
    def parameter(value):
        setattr (Global,'Parameter',value)
    
    def value(value):
        setattr (Global,'Value',value)
        
    def value(value):
        setattr (Global,'Options',value)
        
    def user(value):
        setattr (Global,'User',value)
        
    def prompt(value):
        setattr (Global,'Prompt',value)
        
    def module(module,path):
        setattr (Global,'Module',(module,path))
        
    def payload(payload,path):
        setattr (Global,'Payload',(payload,path))
        
    def defaultpayload(path):
        setattr (Global,'DefaultPayload',path)
        
    def encoder(encoder,path):
        setattr (Global,'Encoder',(encoder,path))