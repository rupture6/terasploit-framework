#######
# Command: Back
#######

from libs.terasploit.framework.command.util.decorator import module_required
from libs.terasploit.framework.opts.opt_container import clean_option
from libs.terasploit.framework.info.info_container import clean_info

from init.tsf.core.wildcard import Set, Get

class _back_:
    
    def cleaner() -> None:
        clean_option(Get.module()[0].module_type)
        clean_info(Get.module()[0].module_type)
    
    @module_required # To notify the user that the command 'back' was executed but there's no current module.
    def function() -> None:
        path = Get.module()[1]
        if 'payload' in path:
            if not Get.payload()[0]:
                _back_.cleaner()
            Set.module(None,None)
            return
        if 'encoder' in path:
            if not Get.encoder()[0]:
                _back_.cleaner()
            Set.module(None,None)
            return
        else:
            _back_.cleaner()
            Set.module(None,None)
            return