#######
# Client: HTTP Client
#######

import requests
from libs.terasploit.framework.formatter.fix_data_type import DataType
from init.teralib.core import Logger

content = {
    'url':None,
    'params':None,
    'data':None,
    'headers':None,
    'cookies':None,
    'files':None,
    'auth':None,
    'timeout':None,
    'proxies':None,
    'verify':None,
    'cert':None,
    'stream':None,
    'json':None
}  

class HTTP:
    """
    HTTP Session for module developers, this will provide a requests session.
    
    >>> print (HTTP.session.get('https://www.google.com'),HTTP.session)
    >>> <Response [200]> <requests.sessions.Session object at 0x7f69bc263a90>
    
    Closing http session will remove the current requests.Session and set
    a new one to be use.
    
    >>> HTTP.new()
    >>> print (HTTP.session.get('https://www.google.com'),HTTP.session)
    >>> <Response [200]> <requests.sessions.Session object at 0x7f69bc3276d0>
    
    HTTP Requests
    
    >>> HTTP.Request('get',url='http://www.google.com)
    >>> <Response [200]>
    """
    
    session = requests.Session()
    
    @classmethod
    def new_session(cls) -> None:
        cls.session.close()
        setattr(HTTP,'session',None)
        setattr(HTTP,'session',requests.Session())
        Logger('info',f"HTTPClient :: HTTP session closed and started a new one.")


    @staticmethod
    def UpdateRequestContent(kwargs):
        """ Update Contents Dictionary """
        
        for i in kwargs:
            content[i] = DataType.float_and_any(kwargs[i])
     
     
    @staticmethod
    def Request(method,url=None,params=None,data=None,headers=None,cookies=None,files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None,stream=None,json=None) -> requests.Response:
        
        """ Usage:
        
        >>> HTTP.Request('http method',**kwargs)
        >>> HTTP.Request('get',url='http://www.google.com)
        >>> <Response [200]>
        """
        
        req_content = {
            'url' : url,
            'params' : params,
            'data' : data,
            'headers' : headers,
            'cookies' : cookies,
            'files' : files,
            'auth' : auth,
            'timeout' : timeout,
            'proxies' : proxies,
            'verify' : verify,
            'cert' : cert,
            'stream' : stream,
            'json' : json
        }
        
        HTTP.UpdateRequestContent(req_content)
        request = getattr(requests,method.lower())
        httprequest = request(
            url=content['url'],
            params=content['params'],
            data=content['data'],
            headers=content['headers'],
            cookies=content['cookies'],
            files=content['files'],
            auth=content['auth'],
            timeout=content['timeout'],
            proxies=content['proxies'],
            verify=content['verify'],
            cert=content['cert'],
            stream=content['stream'],
            json=content['json']
        )
        
        Logger('info',f"HTTPCLient [HTTPRequests] :: '{content['url']}' - {httprequest.status_code}")
        return httprequest