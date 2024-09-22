#######
# Module: Auxiliary
#######

from __future__ import annotations
from libs.terasploit.framework.module.dependencies import *


class Container(object):
    """ Container Descriptor Class """
    
    def __init__(self, value):
        self.value = value
    
    def __get__(self, instance, owner):
        return self.value
    
    
class Insert(Container):
    """ Insert Descriptor Class """
    
    def __set__(self, instance, value):
        self.value = value


class Target:
    """ Target Data """
    
    scheme = Insert(None)
    hostname = Insert(None)
    path = Insert(None)
    params = Insert(None)
    query = Insert(None)
    fragment = Insert(None)
    username = Insert(None)
    password = Insert(None)
    port = Insert(None)


class Auxiliary(object):
    """ Auxiliary Class """

    def GetProxy(self, path: str):
        """ Returns proxy contents from json """
        
        if path:
            with open(path,'r') as prox:
                proxies = json.load(prox)
            info_print (f"Proxies: {proxies}")
        else:
            proxies = {}
        
        return proxies


    def GetBoolean(self, value: str):
        """ Returns boolean value """
        
        if value:
            return True if value.lower() == 'true' else False
        else:
            return True

            
    def ParseURL(self, vals) -> list:
        """ URL Target Parser """
        
        url = urlparse(vals)
        
        value = [url.scheme,url.hostname,url.path,url.params,url.query,url.fragment,url.username,url.password,url.port]
        key = ['scheme','hostname','path','params','query','fragment','username','password','port']
        for key, value in zip(key,value):
            if key == 'hostname':
                if url.hostname:
                    if url.port:
                        setattr(Target,key,f'{value}:{url.port}')
                        continue
                    setattr(Target,key,value)
                if not url.hostname:
                    setattr(Target,'hostname',vals)
            else:        
                setattr(Target,key,value)

        
    def OPT(self):
        """ Returns the value of an option """
        
        opt_content = [x for x in Opt('auxiliary').Get()[0]]
        out = [Opt('auxiliary').GetOPT(x) for x in opt_content]

        return out

        
    def generate_random_name(self) -> str:
        """ Random Name Generator
        
        Generates a random int and str character and put it together to 
        create a random name for files and others.
        """

        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))


    def good_status_code(self) -> list[int]:
        """ Good Status Codes
        
        Returns a good status code, most likely for requests post or get.
        """
        
        return [200,201]
    
    
    def disable_insecure_request_warning(self) -> None:
        """ Insecure request warning
        
        Disables warning from urllib3 that indicates 
        insecure http request.
        """
        
        return urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    
    def pool_manager_cert_required(self,cert_Reqs) -> urllib3.PoolManager:
        """ cert required pool manager - urllib3 """
        
        return urllib3.PoolManager(cert_reqs=cert_Reqs)
    
    
    def SuppressMarkupResemblesLocatorWarning(self) -> warnings.filterwarnings:
        """ BeautifulSoup warning suppressor """
        
        return warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
    
    
    def WaitThreads(self,thread) -> None:
        """ Alive threads waiter """
        
        while thread.is_alive():
            time.sleep(1)
    
    
    def WarningPrint(self, message) -> None:
        """ Prints a warning message """
        
        begin = '\r\b'
        last = '\r'
        header = f'{s.BRIGHT + f.YELLOW}[!]{f.RESET + s.RESET_ALL}'
        sys.stdout.write(f'{begin}{header} {message}.{last}')
        sys.stdout.flush()
        
    
    def GetData(self, path) -> str:
        """ Returns the path of the data file 
        
        >>> self.GetData('data/wordlist/admin/wordlist_adminpanel.txt')
        """
        
        return DataHandler.GetPath(path)
    
    
    def FormatFileContentsToList(self, vals) -> list:
        """ Extracts file contents and return it as list """
        
        contents = []
        file = open(vals,'rb')
        with open(vals, 'rb') as file:
            while line := file.readline():
                contents.append(line.rstrip().decode())
        return contents


    def GetHostByName(self,vals) -> str|any:
        """ Returns ip address """
        
        try:
            return socket.gethostbyname(vals)
        except:
            return vals
        
        
    def hash_md5_(self,word):
        hashed = md5(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest


    def hash_sha1_(self,word):
        hashed = sha1(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest


    def hash_sha224_(self,word):
        hashed = sha224(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest


    def hash_sha256_(self,word):
        hashed = sha256(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest


    def hash_sha384_(self,word):
        hashed = sha384(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest


    def hash_sha512_(self,word):
        hashed = sha512(word.encode())
        digest = hashed.digest()
        hexdigest = hashed.hexdigest()
        return hexdigest, digest