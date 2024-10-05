#######
# Opts: Opt Container
#######

from __future__ import annotations
from init.teralib.base import storedata

class ModuleOptions(object):
    """ Gathers the module options via register option class """
    
    def __init__(self, module: str = None, module_opt: dict = {}) -> None:
        setattr(ModuleOpt,f"{module.lower()}_opt",module_opt)


class register_option(ModuleOptions):
    """ Gathers and pass the module option on ModuleOptions Class for storage
    
    >>> register_option('exploit',opt=[
    >>>     OptIP.create('lhost',['0.0.0.0','yes','the listening address']),
    >>>     OptPort.create('lport',[4444,'yes','the listening port (tcp)'])
    >>> ])
    """
    
    def __init__(self, module: str, opt: list = [], reset: bool = False) -> None:
        if reset == False:
            clean_option(module)
            opts = {}
            for i in opt:
                key = [x for x in i][0]
                opts[key] = i[key]
            super().__init__(module,opts)
            
        if reset == True:
            clean_option(module)


class clean_option:
    """ Cleans the current module option by setting the value to None """
    
    def __init__(self,module_type) -> None:
        option = getattr(ModuleOpt,f"{module_type.lower()}_opt")
        if not option:
            return
        setattr(ModuleOpt,f"{module_type.lower()}_opt",None)
        

class ModuleOpt:
    """ Current module option distributor,
    This is where the current option is stored and accessed. """
    
    auxiliary_opt  =  storedata({})
    exploit_opt    =  storedata({})
    encoder_opt    =  storedata({})
    payload_opt    =  storedata({})

    
class OptIP:
    """ Inserts the ip validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:ip']}
    
    
class OptURL:
    """ Inserts the url validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:url']}


class OptPort:
    """ Inserts the port validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:port']}
    

class OptBool:
    """ Inserts the bool validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:bool']}


class OptInt:
    """ Inserts the int validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:int']}
    

class OptFloat:
    """ Inserts the int validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:float']}
    

class OptFile:
    """ Inserts the file validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:file']}


class OptProxy:
    """ Inserts proxy validation requirement in list """
    
    @staticmethod
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:json']}
    
    
class OptString:
    """ Inserts none validation requirement in list """
    
    @staticmethod    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:none']}
    

class OptValidate:
    """ Creates an option with custom validation """
    
    @staticmethod
    def create(name: str, validate: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:{validate}']}