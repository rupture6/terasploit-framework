#######
# Command: Use
#######

from libs.terasploit.framework.info.info_container import (
    clean_info, 
    module_info
)

from init.tsf.base.wildcard import (
    Paths, 
    Modulizer, 
    Search, 
    value_required, 
    insert_current_payload
)

from init.tsf.ui.wildcard import (
    info_print, 
    f, 
    Table
)

from init.tsf.core.wildcard import (
    Get, 
    Set
)

from init.tsf.util.wildcard import contents
from libs.terasploit.framework.opts.opt_container import clean_option

class _use_:
    
    @value_required
    def function() -> None:
        path = Get.parameter()
        fixed_path = Paths.process_path(path)
        modulize = Paths.pythonize_path(fixed_path)
        
        try:
            module = Modulizer.ImportModule(modulize)()
            _use_.module(module,fixed_path)
            
        except Exception as error:
            if str(error) == "'NoneType' object is not callable":
                info_print (f'Searching {path}...')
                _use_.search(path)
                return
            else:
                info_print (f'Failed to use module, error: {error}')
                return
            
            
    def module(module,path) -> None:
        _, last_module_path = Get.module()
        if last_module_path:
            for i in ['auxiliary','encoder','exploit','payload']:
                if i in last_module_path:
                    clean_info(i)
                    clean_option(i)
                    break
                else:
                    pass
        
        module.initialize()
        Set.module(module,path)
        
        if 'exploit' in path or 'encoder' in path:
            _use_.import_payload()
    
    
    def search(word):
        search_result = Search.search_specific(word)
        
        if not search_result:
            info_print (f"Couldn't find anything related to '{word}'",type='red')
            return
        
        if len(search_result) == 1:
            highlight_word = f.RED + word + f.RESET
            info_print (f"Found match, {search_result[0].replace(word,highlight_word)}",type='green')
            
            fix_found_path = Paths.process_path(search_result[0])
            modulize_found_path = Paths.pythonize_path(fix_found_path)
            found_module = Modulizer.ImportModule(modulize_found_path)()
            
            _use_.module(found_module,fix_found_path)
            return
        
        else:
            tabled_result = Table.module(search_result,'Search',word)
            if tabled_result == False: 
                return
            if tabled_result == True:
                print (contents.interact_message)
                return
            
            
    @insert_current_payload
    def import_payload() -> None:
        try:
            _, path = Get.module()
            if 'exploit' in path:
                normal_path = module_info.exploit_info['Payload']
            if 'encoder' in path:
                normal_path = module_info.encoder_info['Payload']
                
            path = Paths.pythonize_path(normal_path)
            modulize = Modulizer.ImportModule(path)()
            modulize.initialize()
            
            Set.payload(modulize,normal_path)
            info_print (f"Using module default payload, {normal_path.replace('modules/','')}")
        except KeyError:
            info_print ('Payload is missing from the module information',type='YELLOW')