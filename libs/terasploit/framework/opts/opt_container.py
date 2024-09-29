#######
# Opts: Opt Container
#######

from __future__ import annotations


class OptionsContainer(object):
    """ Contains the current module options dictionary """
    
    def __init__(self,opt=None) -> None:
        """ init function to get the opt """
        
        self.opt = opt
        
    def __get__(self, instance, owner) -> any|None:
        """ get descriptor to return the current module options """

        return self.opt


class InsertOption(OptionsContainer):
    """ Inserts the current module options in options container """
    
    def __set__(self, instance, value) -> None:
        """ set descriptor to store the currnt module options """
        
        self.opt = value


class ModuleOptions(object):
    """ Gathers the module options via register option class """
    
    def __init__(self, module: str = None, module_opt: dict = {}) -> None:
        setattr(ModuleOpt,f"{module.lower()}_opt",module_opt)


class register_option(ModuleOptions):
    """ Gathers and pass the module option on ModuleOptions Class for storage
    
    >>> register_option('exploit',opt=[
    >>>     OptIP.create('lhost',['0.0.0.0','yes','target listening address']),
    >>>     OptPort.create('lport',[4444,'yes','target listening port'])
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
    """ Current module option distributor -- 
    This is where the current option is stored to be accessed. """
    
    auxiliary_opt = InsertOption()
    exploit_opt = InsertOption()
    encoder_opt = InsertOption()
    payload_opt = InsertOption()

    
class OptIP:
    """ Inserts the ip validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:ip']}
    
    
class OptURL:
    """ Inserts the url validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:url']}


class OptPort:
    """ Inserts the port validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:port']}
    

class OptBool:
    """ Inserts the bool validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:bool']}


class OptInt:
    """ Inserts the int validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:int']}
    

class OptFloat:
    """ Inserts the int validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:float']}


class OptFile:
    """ Inserts the file validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,'validate:file']}


class OptProxy:
    """ Inserts proxy validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:json']}
    
    
class OptString:
    """ Inserts none validation requirement in list """
    
    def create(name: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:none']}
    

class OptValidate:
    
    def create(name: str, validate: str, opt: list) -> dict[str, list]: 
        return {name:[opt,f'validate:{validate}']}