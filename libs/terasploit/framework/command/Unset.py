#######
# Command: Unset
#######

from libs.terasploit.framework.info.info_container import clean_info
from libs.terasploit.framework.opts.opt_container import clean_option
from libs.terasploit.framework.opts.opt_distributor import (
    Opt,
    ModuleOpt
)
from libs.terasploit.framework.command import Use
from init.teralib.core import (
    Get,
    Set
)
from init.teralib.base import (
    TerasploitInvalidOption,
    param_required,
    encoder_required,
    payload_required,
)
from init.teralib.ui import print_info

# Command class

class _unset_:
    
    @staticmethod
    @param_required
    def function() -> None:
        global_variables = Get.globalvariables()
        parameter = Get.parameter()
        
        if parameter in global_variables:
            _unset_.global_opt()
            return
        else:
            _unset_.module_opt()
            return
    
    
    @staticmethod
    @encoder_required
    def global_encoder() -> None:
        parameter = Get.parameter()
        
        print (f'unset => {parameter}')
        Set.encoder(None,None)
        clean_option('payload')
        clean_info('payload')


    @staticmethod
    @payload_required
    def global_payload() -> None:
        module, _ = Get.module()
        parameter = Get.parameter()

        Set.payload(None,None)
        clean_option('payload')
        clean_info('payload')
        
        print (f'unset => {parameter}')
            
        if module:
            try:
                Use._use_.import_payload()
                print_info('Unset done, used module default payload. If this is a mistake, do not unset payload while a module is in use, set a new one instead.',type='yellow')
            except:
                return
        
    
    @staticmethod
    def global_opt() -> None:
        parameter = Get.parameter()
        
        if hasattr(_unset_,f'global_{parameter.lower()}'):
            global_unset = getattr(_unset_,f'global_{parameter.lower()}')
            global_unset()
            return
        else:
            if parameter.lower() == 'user':
                Set.user('')
            if parameter.lower() == 'prompt':
                Set.prompt('')
            print (f"unset => {parameter}")
    
    
    @staticmethod
    def unset_module_opt(type,parameter,value) -> None:
        if type == 'auxiliary':
            ModuleOpt.auxiliary_opt[parameter][0][0] = value
        if type == 'encoder':
            ModuleOpt.encoder_opt[parameter][0][0] = value
        if type == 'exploit':
            ModuleOpt.exploit_opt[parameter][0][0] = value
        if type == 'payload':
            ModuleOpt.payload_opt[parameter][0][0] = value
            

    @staticmethod
    def module_opt() -> None:
        parameter = Get.parameter().lower()
        available_set = 0
        
        for i in ['auxiliary','encoder','exploit','payload']:
            if Opt(i).Get()[0]:
                opt_owner = getattr(ModuleOpt,f'{i}_opt')

                if opt_owner.get(parameter):
                    available_set += 1
                    _unset_.unset_module_opt(i,parameter,'')
                    print (f"unset => {parameter}")
                else:
                    continue
            else:
                continue
        
        if available_set == 0:
            raise TerasploitInvalidOption(parameter,"An invalid option was specified, failed to set value.")