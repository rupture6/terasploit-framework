#######
# Core: Contents Dispatcher
#######

from libs.tsf.core.contents_container import Global

class Get:
    """ Get - Access a value from global handler and return it to the functions that required it """
    
    @staticmethod
    def command() -> str:
        return Global.Command


    @staticmethod
    def parameter() -> str:
        return Global.Parameter


    @staticmethod
    def value() -> str:
        return Global.Value
    
    
    @staticmethod
    def options() -> str:
        return Global.Options
    
    
    @staticmethod
    def user() -> str:
        return Global.User
    
    
    @staticmethod
    def prompt() -> str:
        return Global.Prompt
    
    
    @staticmethod
    def globalvariables() -> list:
        return Global.GlobalVariables
    
    
    @staticmethod
    def module() -> tuple[any,any]: 
        module, path = Global.Module
        return module, path
    
    
    @staticmethod
    def payload() -> tuple[any,any]:
        payload, path = Global.Payload
        return payload, path
    
    
    @staticmethod
    def encoder() -> tuple[any,any]:
        encoder, path = Global.Encoder
        return encoder, path
    
    
class Set:
    """ Set - Changes values from non-static variables of global handler """
    
    @staticmethod
    def command(value):
        setattr (Global,'Command',value)
    
    
    @staticmethod
    def parameter(value):
        setattr (Global,'Parameter',value)
    
    
    @staticmethod
    def value(value):
        setattr (Global,'Value',value)
        
        
    @staticmethod
    def value(value):
        setattr (Global,'Options',value)
        
        
    @staticmethod
    def user(value):
        setattr (Global,'User',value)
    
    
    @staticmethod
    def prompt(value):
        setattr (Global,'Prompt',value)
    
    
    @staticmethod
    def module(module,path):
        setattr (Global,'Module',(module,path))
    
    
    @staticmethod
    def payload(payload,path):
        setattr (Global,'Payload',(payload,path))
        
        
    @staticmethod
    def defaultpayload(path):
        setattr (Global,'DefaultPayload',path)
        
        
    @staticmethod
    def encoder(encoder,path):
        setattr (Global,'Encoder',(encoder,path))