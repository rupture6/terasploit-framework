#######
# Command: Info
#######

from libs.terasploit.framework.info.info_container import module_info
from init.tsf.core.wildcard import Get

from init.tsf.ui.wildcard import (
    Table, 
    line_break, 
    info_print
)

from init.tsf.base.wildcard import (
    Modulizer, 
    Paths, 
    value_required, 
    module_required
)

class _info_:

    def function() -> None:
        module, _ = Get.module()
        payload, _ = Get.payload()
        encoder, _ = Get.encoder()
        parameter = Get.parameter()
        
        if parameter:
            _info_.unused_module()
            if 'payload' in parameter:
                if payload:
                    payload.initialize(info_only=True)
            if 'encoder' in parameter:
                if encoder:
                    encoder.initialize(info_only=True)
            if 'payload' or 'encoder' not in parameter:
                if module:
                    module.initialize(info_only=True)
            return
        
        _info_.module()
        
    
    @value_required
    def unused_module():
        parameter = Get.parameter()
        path = Paths.process_path(parameter)
        modulize = Paths.pythonize_path(path)
        try:
            module = Modulizer.ImportModule(modulize)()
        except:
            info_print ('Failed to get full module information.',type='red')
            return
        
        module.initialize(info_only=True)
        for info in [module_info.auxiliary_info,module_info.encoder_info,module_info.exploit_info,module_info.payload_info]:
            if info:
                if info['Module'] == 'payload':
                    line_break()
                    print ('Payload Information')
                    print ('===================')
                    line_break()
                if info['Module'] != 'payload':
                    line_break()
                    print ('Module Information')
                    print ('==================')
                    line_break() 
                Table.info_table(info.items())
        

    @module_required
    def module():
        for info in [module_info.auxiliary_info,module_info.encoder_info,module_info.exploit_info,module_info.payload_info]:
            if info:
                if info['Module'] == 'payload':
                    line_break()
                    print ('Payload Information')
                    print ('===================')
                    line_break()
                if info['Module'] != 'payload':
                    line_break()
                    print ('Module Information')
                    print ('==================')
                    line_break() 
                Table.info_table(info.items())
        return