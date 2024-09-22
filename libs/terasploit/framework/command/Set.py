#######
# Command: Set
#######

from libs.terasploit.framework.command.util.decorator import (
    param_required, 
    value_required
)

from libs.terasploit.framework.opts.opt_container import ModuleOpt
from libs.terasploit.framework.opts.opt_distributor import Opt

from init.tsf.ui.wildcard import info_print
from init.tsf.core.wildcard import (
    Get, 
    Set
)

from init.tsf.base.wildcard import (
    Paths, 
    Modulizer, 
    validator, 
    TerasploitInvalidOption
)
    
class _set_:    
    
    @param_required
    @value_required
    def function() -> None:
        global_variables = Get.globalvariables()
        parameter = Get.parameter()
        
        if parameter in global_variables:
            _set_.global_opt()
            return
        else:
            _set_.module_opt()
            return
        
    
    def global_payload() -> None:
        payload_path = Get.value()
        
        process_path = Paths.process_path(payload_path)
        path = Paths.pythonize_path(process_path)

        try:
            modulize = Modulizer.ImportModule(path)()
            modulize.initialize()
            Set.payload(modulize,process_path)
            print (f'payload =>',payload_path.replace('modules/',''))
        except:
            return
    
    
    def global_encoder() -> None:
        encoder_path = Get.value()
        
        process_path = Paths.process_path(encoder_path)
        path = Paths.pythonize_path(process_path)

        try:
            modulize = Modulizer.ImportModule(path)()
            modulize.initialize()
            if hasattr(modulize,'encode'):
                Set.encoder(modulize,process_path)
                print (f'encoder =>',encoder_path.replace('modules/',''))
            else:
                info_print ('Invalid encoder module.',type='red')
                return
        except:
            return


    def global_opt() -> None:
        parameter = Get.parameter()
        value = Get.value()
        
        if hasattr(_set_,f'global_{parameter.lower()}'):
            global_set = getattr(_set_,f'global_{parameter.lower()}')
            global_set()
            return
        else:
            if parameter.lower() == 'user':
                Set.user(value)
            if parameter.lower() == 'prompt':
                Set.prompt(value)
            print (f"{parameter} => {value}")
            
            
    def set_opt(type,parameter,value) -> None:
        if type == 'auxiliary':
            ModuleOpt.auxiliary_opt[parameter][0][0] = value
        if type == 'encoder':
            ModuleOpt.encoder_opt[parameter][0][0] = value
        if type == 'exploit':
            ModuleOpt.exploit_opt[parameter][0][0] = value
        if type == 'payload':
            ModuleOpt.payload_opt[parameter][0][0] = value
        
    
    def validation_process(module_type,parameter,value,validation) -> None:
        _,validate = validation.split(':')
        if validate == 'none':
            _set_.set_opt(module_type,parameter,value)
            print (f'{parameter} => {value}')
            return
            
        opt_validator = getattr(validator,f'validate_{validate}_')
        opt_validation = opt_validator(value)
        
        if opt_validation == True:
            _set_.set_opt(module_type,parameter,value)
            print (f'{parameter} => {value}')
            return
        if opt_validation == False:
            print (f"{parameter} => invalid: '{value}'")
            return
            
    
    def module_opt() -> None:
        parameter = Get.parameter().lower()
        value = Get.value()
        
        available_set = 0
        
        for i in ['auxiliary','encoder','exploit','payload']:
            if Opt(i).Get()[0]:
                opt_owner = getattr(ModuleOpt,f'{i}_opt')

                if opt_owner.get(parameter):
                    available_set += 1
                    validation = opt_owner[parameter][-1]
                    _set_.validation_process(i,parameter,value,validation)
                else:
                    continue
            else:
                continue
        
        if available_set == 0:
            raise TerasploitInvalidOption(parameter,"An invalid option was specified, failed to set value.")