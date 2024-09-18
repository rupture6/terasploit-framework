#######
# Client: HTTP Client
#######

import requests

from init.tsf.ui.wildcard import info_print
from init.tsf.core.wildcard import Logger
from init.terasploit.framework.formatter.wildcard import DataType

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
    """ HTTP Session Class
    
    HTTP Session for module developers, this will provide a requests session.
    
    >>> print (HTTPSession.session.get('https://www.google.com'),HTTPSession.session)
    >>> <Response [200]> <requests.sessions.Session object at 0x7f69bc263a90>
    
    Closing http session will remove the current requests.Session and set
    a new one to be use.
    
    >>> HTTP().new()
    >>> print (HTTPSession.session.get('https://www.google.com'),HTTPSession.session)
    >>> <Response [200]> <requests.sessions.Session object at 0x7f69bc3276d0>
    """
    
    session = requests.Session()
    
    def new(self) -> None:
        self.session.close()
        setattr(HTTP,'session',None)
        setattr(HTTP,'session',requests.Session())
        Logger('info',f"HTTPClient :: HTTP session closed and started a new one.")


class HTTPClient:
    """ Http Client Class -- Handler of http request connection """
    
    def UpdateRequestContent(kwargs):
        """ Update Contents Dictionary """
        
        for i in kwargs:
            content[i] = DataType.float_and_any(kwargs[i])
     
     
    def Request(method,url=None,params=None,data=None,headers=None,cookies=None,files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None,stream=None,json=None) -> requests.Response:
        
        """ Usage:
        
        Just like a normal requests.get(url,params=params,files=files,...) to use
        this, it's much similar to requests.Request where you put the method to use.
        However, the difference is requests.Request has a limited arguments compared
        to this function.
        
        >>> HTTPClient.Request('get',url='http://www.google.com)
        >>> <Response [200]>
        
        WARNING: 
        
            In url, you need to put an equal sign to it before the value because
            the function only accepts **kwargs, so if you directly put the url, 
            it will have an error indicating that Request got an invalid argument.
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
        HTTPClient.UpdateRequestContent(req_content)

        info_print (f'Sending {method.lower()} request...')
        request = getattr(requests,method.lower())
        result = request(
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
        
        Logger('info',f"HTTPCLient [HTTPRequests] :: '{content['url']}' - {result.status_code}")
        return result