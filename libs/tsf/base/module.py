#######
# Base: Module
#######

from __future__ import annotations

import importlib

from init.tsf.ui.wildcard import *
from libs.tsf.base.exception import TerasploitModuleError, TerasploitException

class Modulizer:
    def Import(path: str):
        try:
            Module = importlib.import_module(path)
            return Module
        except Exception as error:
            if 'No module named' in str(error):
                info_print (f"There is no module '{path.replace('.','/').replace('modules/','')}'",type='RED')
                return None
            else:
                info_print (f"Module error: {error}",type='RED')
                return None
            
            
    def ImportModule(path: str) -> any|None:
        try:
            attributes = ['TerasploitExploit','TerasploitAuxiliary','TerasploitEncoder','TerasploitPayload']
            module = Modulizer.Import(path)
            if not module:
                return None
        
            for module_attribute in attributes:
                if hasattr(module,module_attribute):
                    return getattr(module,module_attribute)

            raise TerasploitModuleError(path.replace('.','/').replace('modules/',''),f"Unknown Module: {path.replace('.','/')}")
        except TerasploitException:
            return None