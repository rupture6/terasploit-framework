#######
# Info: Info Container
#######

from __future__ import annotations
from init.teralib.base import storedata

class module_info:
    """ Information containers """
    
    auxiliary_info  =  storedata({})
    encoder_info    =  storedata({})
    exploit_info    =  storedata({})
    payload_info    =  storedata({})
        
        
def clean_info(module) -> None:
    """ Cleans the module info """
    
    info = getattr(module_info,f"{module.lower()}_info")
    if not info:
        return
    setattr(module_info,f"{module.lower()}_info",None)
    
    
def update_info(info: dict = {}) -> None:
    """ Updates the module info """
    
    clean_info(info['Module'])
    setattr(module_info,f"{info['Module'].lower()}_info",info)