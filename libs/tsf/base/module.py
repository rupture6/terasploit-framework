#######
# Base: Module
#######

from __future__ import annotations

import importlib
from init.teralib.ui import print_info
from libs.tsf.base.exception import (
    TerasploitModuleError,
    TerasploitException
)

class Modulizer:
    
    @staticmethod
    def Import(path: str):
        try:
            Module = importlib.import_module(path)
            return Module
        
        except Exception as error:
            if 'No module named' in str(error):
                print_info (f"There is no module '{path.replace('.','/').replace('modules/','')}'",type='RED')
                return
            else:
                print_info (f"Module error: {error}",type='RED')
                return
            
    
    @staticmethod
    def ImportModule(path: str) -> any|None:
        try:
            attribute = ['TerasploitModule','TerasploitPayload']
            module = Modulizer.Import(path)
            if not module:
                return
            
            for attr in attribute:
                if hasattr(module,attr):
                    return getattr(module,attr)

            raise TerasploitModuleError(path.replace('.','/').replace('modules/',''),f"Unknown Module: {path.replace('.','/')}")
        except TerasploitException:
            return