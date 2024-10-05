#######
# Command: Info
#######

from libs.terasploit.framework.info.info_container import module_info
from init.teralib.base import (
    Modulizer,
    Paths,
    module_required,
    value_required
)
from init.teralib.core import Get
from init.teralib.ui import (
    Table,
    line_break,
    print_info
)

# Command class

class _info_:

    @staticmethod
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
        
        
    @staticmethod
    @value_required
    def unused_module():
        parameter = Get.parameter()
        path = Paths.process_path(parameter)
        modulize = Paths.pythonize_path(path)
        try:
            module = Modulizer.ImportModule(modulize)()
        except:
            print_info ('Failed to get full module information.',type='red')
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
        

    @staticmethod
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