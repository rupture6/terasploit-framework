#######
# Info: Info Container
#######

from __future__ import annotations
from init.tsf.core.wildcard import Get


class InfoContainer(object):
    """ Contains the information of the module """
    
    def __init__(self,dictionary) -> None:
        self.dictionary = dictionary
        
    def __get__(self,instance,owner) -> dict:
        return self.dictionary
    
    
class InfoInsert(InfoContainer):
    """ Inserts the info in InfoContainer Class to be accessed later """
    
    def __set__(self,instance,value) -> None:
        self.dictionary = value
        

class module_info:
    """ Handler of Descriptor Classes """
    
    auxiliary_info = InfoInsert({})
    encoder_info = InfoInsert({})
    exploit_info = InfoInsert({})
    payload_info = InfoInsert({})
        
        
class clean_info:
    """ Cleans the module info """
    
    def __init__(self,module):
        info = getattr(module_info,f"{module.lower()}_info")
        if not info:
            return
        setattr(module_info,f"{module.lower()}_info",None)


class update_info(module_info):
    """ Module information updater """
    
    def __init__(self,info: dict = {}) -> None:
        clean_info(info['Module'])
        setattr(module_info,f"{info['Module'].lower()}_info",info)
        return