#######
# Command: Use
#######

from libs.terasploit.framework.command.util.decorator import value_required, module_insert_payload
from libs.terasploit.framework.opts.opt_container import clean_option
from libs.terasploit.framework.info.info_container import clean_info

from init.tsf.base.wildcard import Paths, Modulizer, Search
from init.tsf.ui.wildcard import info_print, f, Table
from init.tsf.util.wildcard import contents
from init.tsf.core.wildcard import Get, Set

class _use_:
    
    @value_required
    def function() -> None:
        path = Get.parameter()
        
        fixed_path = Paths.process_path(path)
        modulize = Paths.pythonize_path(fixed_path)
        
        try:
            module = Modulizer.ImportModule(modulize)()
            module.initialize()
            _use_.module(module,fixed_path)
        except:
            info_print(f'Searching {path}...')
            _use_.search(path)
            
            
    def module(module,path) -> None:
        last_module, _ = Get.module()
        if last_module:
            clean_option(last_module.module_type)
            clean_info(last_module.module_type)
        
        Set.module(module,path)
        current_module, _ = Get.module()
        encoder, _ = Get.encoder()
        
        if hasattr(current_module,'payload'):
            _use_.import_payload()

        if hasattr(current_module,'encoder'):
            if encoder:
                setattr(current_module,'encoder',encoder)
    
    
    def search(word):
        search_result = Search.search_specific(word)
        
        if not search_result:
            info_print (f"Couldn't find anything related to '{word}'",type='red')
            return
        
        if len(search_result) == 1:
            highlight_word = f.RED + word + f.RESET
            info_print (f"Found match: {search_result[0].replace(word,highlight_word)}",type='green')
            fix_found_path = Paths.process_path(search_result[0])
            modulize_found_path = Paths.pythonize_path(fix_found_path)
            found_module = Modulizer.ImportModule(modulize_found_path)()
            found_module.initialize()
            _use_.module(found_module,fix_found_path)
            
            return
        
        else:
            tabled_result = Table.module(search_result,'Search',word)
            if tabled_result == False: 
                return
            if tabled_result == True:
                print (contents.interact_message)
                return
            
            
    @module_insert_payload
    def import_payload() -> None:
        module, _ = Get.module()
        if not hasattr(module,'payload'):
            return

        normal_path = module.payload
        Set.defaultpayload(normal_path)
        path = Paths.pythonize_path(normal_path)
        
        try:
            modulize = Modulizer.ImportModule(path)()
            modulize.initialize()
            Set.payload(modulize,normal_path)
            payload, _ = Get.payload()

            setattr(module,'payload',payload)
            info_print('No current payload specified, using module default payload.')
        except:
            return