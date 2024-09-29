#######
# Command: Back
#######

from libs.terasploit.framework.opts.opt_container import clean_option
from libs.terasploit.framework.info.info_container import clean_info

from init.tsf.base.wildcard import module_required
from init.tsf.core.wildcard import Set, Get

class _back_:
    
    def cleaner(module) -> None:
        clean_option(module)
        clean_info(module)
    
    @module_required # To notify the user that the command 'back' was executed but there's no current module.
    def function() -> None:
        _, path = Get.module()
        
        if 'encoder' in path:
            if not Get.encoder()[0]:
                _back_.cleaner('encoder')
            Set.module(None,None)
            return
        
        if 'payload' in path:
            if not Get.payload()[0]:
                _back_.cleaner('payload')
            Set.module(None,None)
            return
        
        if 'auxiliary' in path:
            _back_.cleaner('auxiliary')
            Set.module(None,None)
            return
        
        if 'exploit' in path:
            _back_.cleaner('exploit')
            _back_.cleaner('payload')
            Set.module(None,None)
            Set.payload(None,None)
            return