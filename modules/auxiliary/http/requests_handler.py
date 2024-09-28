#######
# Module/Auxiliary: XSS Query Inject via HTTP Requests
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):

    content = {'url':None,'params':None,'data':None,'headers':None,'cookies':None,'files':None,'auth':None,'timeout':None,'proxies':None,'verify':None,'cert':None,'stream':None,'json':None}
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'License'       : 'Terasploit Framework License (BSD)',
                'Module'        : Module.auxiliary,
                'Name'          : 'HTTP Requests Handler via Yaml Config',
                'Version'       : '1.0',
                'Author'        : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Documentation' : [
                    'https://github.com/rupture6/terasploit-framework/blob/master/documentation/modules/requests_handler.md',
                ],
                'Description'   : [
                    'Versatile module that allows a user to use requests library',
                    'for web exploitation via yaml file config'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptValidate.new('config','yaml',['','yes','yaml config to read']),
            OptBool.new('session',['false','yes','use http request session'])
        ])

    
    def display_result(self,method,result) -> None:
        info_print ('Displaying response returned...')
        print (f"{method.upper()} {result.request.url}")
        print (f"Status-Code: {result.status_code}")
        print ('-- Headers --')
        print ('\r\n'.join('{}: {}'.format(k, v) for k, v in result.request.headers.items()))
        print ('-- Body --')
        print (result.request.body)
    
    
    def http_session(self,method) -> None:
        Session = getattr(HTTP.session,method.lower())
        response = Session(
            url=self.content['url'],
            params=self.content['params'],
            data=self.content['data'],
            headers=self.content['headers'],
            cookies=self.content['cookies'],
            files=self.content['files'],
            auth=self.content['auth'],
            timeout=self.content['timeout'],
            proxies=self.content['proxies'],
            verify=self.content['verify'],
            cert=self.content['cert'],
            stream=self.content['stream'],
            json=self.content['json']
        )
        self.display_result(method,response)
    
    
    def http_no_session(self,method) -> None:
        response = HTTPClient.Request(
            method,
            url=self.content['url'],
            params=self.content['params'],
            data=self.content['data'],
            headers=self.content['headers'],
            cookies=self.content['cookies'],
            files=self.content['files'],
            auth=self.content['auth'],
            timeout=self.content['timeout'],
            proxies=self.content['proxies'],
            verify=self.content['verify'],
            cert=self.content['cert'],
            stream=self.content['stream'],
            json=self.content['json']
        )
        self.display_result(method,response)


    def run(self) -> None:
        file, session = self.OPT()
        try:
            with open(file) as yml:
                content = yaml.safe_load(yml)
            for i in content['content']:
                if i.lower() == 'method':
                    pass
                self.content[i.lower()] = content['content'][i]
            if session.lower() == 'false':
                self.http_no_session(method=content['content']['method'])
            if session.lower() == 'true':
                self.http_session(method=content['content']['method'])
                
            return 'done', True
        except Exception as error:
            info_print(error, type='red')
            return 'exception', True