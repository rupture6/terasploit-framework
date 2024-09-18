#######
# Module/Auxiliary: XSS Query Inject via HTTP Requests
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitAuxiliary(Auxiliary):
    
    module_type = 'auxiliary'
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : 'auxiliary',
                'Name' : 'XSS Query Inject via HTTP Requests',
                'Author' : 'Handler4',
                
                'Description' : [
                    'XSS vulnerability scanner. It scans for xss vulnerability',
                    'by injecting xss payload in url queries. It uses http request',
                    'to inject the target with xss payload, if status code is good,',
                    'it will check the sourcecode to validate the xss payload',
                    'injection.',
                ],
                
                'Warning' : 'Green results are sometimes false positive.'
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptFile.new('target',['','yes','text file containing a list of target(s)']),
            OptFile.new('xss_payload',['','no','text file containing a list of xss payloads']),
            OptString.new('method','http_method',['get','yes','http method to use in http request']),
            OptString.new('query','none',['id','yes','query key to attempt payload injection'])
        ])
    
    def run(self) -> tuple[str, bool]: 
        targets = self.GetOPT('target')
        xss_payload = self.GetOPT('xss_payload')
        method = self.GetOPT('method')
        query = self.GetOPT('query')
        
        path = self.GetData('data/wordlist/xss/wordlist_payload.txt')
        payload_file = xss_payload if xss_payload else path
        
        target_list = self.FormatFileContentsToList(targets)
        payload_list = self.FormatFileContentsToList(payload_file)
        
        self.SuppressMarkupResemblesLocatorWarning()
        
        for target in target_list:
            info_print (f'Current target: {target}')
            info_print ('Testing xss payloads...')
            for payload in payload_list:
                try:
                    scan = HTTPClient.Request(method.lower(),url=target,params={query:payload})
                    if scan.status_code in self.good_status_code():
                        scrape = BeautifulSoup(scan.content,features='lxml')
                        found = scrape.find()
                        if payload not in found.get_text():
                            if payload in scan.text:
                                info_print (f'Try Payload: {payload}',type='green')
                            if payload not in scan.text:
                                info_print (f"Payload not found in sourcecode: {payload}")
                        if payload in found.get_text():
                            info_print (f"Found payload as text in sourcecode: {payload}",type='yellow')                    
                    else:
                        info_print (f'Status code: {scan.status_code}, failed to inject payload: {payload}',type='red')

                except Exception as error:
                    if 'Invalid URL' in str(error):
                        info_print (f'Invalid URL detected: {target}',type='red')
                        break
                    info_print (error,type='red')
                    break
                
        return 'done', True