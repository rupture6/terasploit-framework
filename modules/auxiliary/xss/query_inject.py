#######
# Module/Auxiliary: XSS Query Inject via HTTP Requests
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
                'Name'        : 'XSS Query Inject via HTTP Requests',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'XSS vulnerability scanner. It scans for xss vulnerability',
                    'by injecting xss payload in url queries. It uses http request',
                    'to inject the target with xss payload, if status code is good,',
                    'it will check the sourcecode to validate the xss payload',
                    'injection. Note, green results are sometimes false positive.'
                ],
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptFile.create('targetlist',['','yes','text file containing a list of target(s)']),
            OptFile.create('xss_payload',['','no','text file containing a list of xss payloads']),
            OptValidate.create('method','http_method',['get','yes','http method to use in http request']),
            OptString.create('query',['id','yes','query key to attempt payload injection'])
        ])
    
    def run(self) -> tuple[str, bool]: 
        targets, xss_payload, method, query = self.OPT()
        
        path = self.GetData('data/wordlist/xss/wordlist_payload.txt')
        payload_file = xss_payload if xss_payload else path
        
        target_list = self.FormatFileContentsToList(targets)
        payload_list = self.FormatFileContentsToList(payload_file)
        
        self.SuppressMarkupResemblesLocatorWarning()
        
        for target in target_list:
            print_info (f'Current target: {target}')
            print_info ('Testing xss payloads...')
            for payload in payload_list:
                try:
                    scan = HTTP.Request(method.lower(),url=target,params={query:payload})
                    if scan.status_code in self.good_status_code():
                        scrape = BeautifulSoup(scan.content,features='lxml')
                        found = scrape.find()
                        if payload not in found.get_text():
                            if payload in scan.text:
                                print_info (f'Try Payload: {payload}',type='green')
                                print_info (f'Current target: {target}')
                            if payload not in scan.text:
                                print_info (f"Payload not found in sourcecode: {payload}")
                        if payload in found.get_text():
                            print_info (f"Found payload as text in sourcecode: {payload}",type='yellow')                    
                    else:
                        print_info (f'Status code: {scan.status_code}, failed to inject payload: {payload}',type='red')

                except Exception as error:
                    if 'Invalid URL' in str(error):
                        print_info (f'Invalid URL detected: {target}',type='red')
                        break
                    print_info (error,type='red')
                    break
        return