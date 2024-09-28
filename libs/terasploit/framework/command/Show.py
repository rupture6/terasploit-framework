#######
# Command: Show
#######

from init.tsf.ui.wildcard import (
    Table, 
    info_print, 
    line_break
)

from init.tsf.base.wildcard import (
    Search,
    param_required
)

from init.tsf.core.wildcard import Get
from init.tsf.util.wildcard import contents
from config.module_config import directories

from libs.terasploit.framework.opts.opt_distributor import Opt

class _show_:
    
    @param_required
    def function() -> None:
        query = Get.parameter()
        show_parameters = 'all, options, exploit, auxiliary, payload, encoder'
        
        if hasattr(_show_,f"{query.lower()}"):
            sub_function = getattr(_show_, f"{query.lower()}")
            sub_function()
            return
        
        elif query in directories.get():
            result = Search.search_specific(query)
            tabled_result = Table.module(result,'Show',query)
            if tabled_result == False: 
                return
            if tabled_result == True:
                print (contents.interact_message)
                return
            
        elif query not in directories.get():
            info_print ("Invalid show parameter '" + query + "', parameters: " + str(show_parameters),type='red')
            return
        
        
    def all() -> None:
        result = Search.all_modules()
        Table.all_module(result)
        print (contents.interact_message)
        
    
    def options() -> None:
        module, _ = Get.module()
        if not module:
            _show_.global_opt()

        _show_.module_opt()
        
        
    def global_opt() -> None:
        user = Get.user()
        prompt = Get.prompt()
        _, payload_path = Get.payload()
        _, encoder_path = Get.encoder()

        Name = ['user','prompt','payload','encoder']
        Value = [str(user),str(prompt),str(payload_path),str(encoder_path)]
        Description = [
            'the prompt user',
            'the prompt character',
            'current configured payload module',
            'current configured encoder module'
        ]
        Table.global_option(Name,Value,Description)
        
        
    def auxiliary_opt() -> None:
        _, path = Get.module()
        opt_name = [x for x in Opt('auxiliary').Get()[0]]
        opt_contents = []
        
        for i in opt_name:
            opt_contents.append([x for x in [x for x in Opt('auxiliary').Get()[0][i][0]]])
        
        opt_value = [opt[0] for opt in opt_contents]
        opt_required = [opt[1] for opt in opt_contents]
        opt_description = [opt[2] for opt in opt_contents]
        
        Table.module_option('Auxiliary',path,opt_name,opt_value,opt_required,opt_description)
        
        
    def encoder_opt() -> None:
        _, path = Get.payload() if Get.encoder()[0] else Get.module()
        
        opt_name = [x for x in Opt('encoder').Get()[0]]
        opt_contents = []
        
        for i in opt_name:
            opt_contents.append([x for x in [x for x in Opt('encoder').Get()[0][i][0]]])
        
        opt_value = [opt[0] for opt in opt_contents]
        opt_required = [opt[1] for opt in opt_contents]
        opt_description = [opt[2] for opt in opt_contents]
        
        Table.module_option('Encoder',path,opt_name,opt_value,opt_required,opt_description)
        
    
    def exploit_opt() -> None:
        _, path = Get.module()
        opt_name = [x for x in Opt('exploit').Get()[0]]
        opt_contents = []
        
        for i in opt_name:
            opt_contents.append([x for x in [x for x in Opt('exploit').Get()[0][i][0]]])
        
        opt_value = [opt[0] for opt in opt_contents]
        opt_required = [opt[1] for opt in opt_contents]
        opt_description = [opt[2] for opt in opt_contents]
        
        Table.module_option('Exploit',path,opt_name,opt_value,opt_required,opt_description)
        

    def payload_opt() -> None:
        _, path = Get.payload() if Get.payload()[0] else Get.module()
        opt_name = [x for x in Opt('payload').Get()[0]]
        opt_contents = []
        
        for i in opt_name:
            opt_contents.append([x for x in [x for x in Opt('payload').Get()[0][i][0]]])
        
        opt_value = [opt[0] for opt in opt_contents]
        opt_required = [opt[1] for opt in opt_contents]
        opt_description = [opt[2] for opt in opt_contents]
        
        Table.module_option('Payload',path,opt_name,opt_value,opt_required,opt_description)
        
    
    def module_opt() -> None:
        not_available = 0

        for available, module in [Opt('auxiliary').Get(),Opt('encoder').Get(),Opt('exploit').Get(),Opt('payload').Get()]:
            if not available:
                not_available += 1
                continue
            getattr(_show_,f"{module}_opt")()

        if not_available != 4:
            print (contents.module_info)
            line_break()
            return
        
        Table.module_option('No available module','/',[''],[''],[''],[''])