#######
# Module: Auxiliary
#######

from __future__ import annotations

import sys
import urllib3
import requests
import socket
import random
import string
import warnings
import threading
import time
import traceback
import yaml
import base64
import re

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
from requests.auth import HTTPDigestAuth

from data.data_handler import DataHandler

from libs.terasploit.framework.opts.opt_distributor import Opt
from libs.terasploit.framework.clients.utils.familiy_address import AddrFam
from libs.terasploit.framework.clients.utils.socket_kind import SockType
from libs.terasploit.framework.clients.utils.error_codes import tcp_error_codes, udp_error_codes
from libs.terasploit.framework.formatter.fix_data_type import DataType

from init.terasploit.framework.clients.wildcard import *
from init.tsf.ui.wildcard import info_print, f, b, s, clean_last_line

from init.terasploit.framework.clients.wildcard import (
    HTTP,
    HTTPClient,
    TCPClient,
    UDPClient,
    SOCKClient
)

__all__ = [
    'Opt',
    'Auxiliary',
    'info_print',
    'HTTP',
    'HTTPClient',
    'TCPClient',
    'UDPClient',
    'SOCKClient',
    'AddrFam',
    'SockType',
    'DataType',
    'tcp_error_codes',
    'udp_error_codes',
    'f',
    's',
    'b',
    'clean_last_line',
    
    'HTTPDigestAuth',
    'BeautifulSoup',
    'requests',
    'socket',
    'threading',
    'traceback',
    'yaml',
    'time',
    'base64',
    're'
]

class Auxiliary(object):

    def GetOPT(self, opt: str):
        """ Returns the value of an option """
        
        return Opt('auxiliary').GetOPT(opt)
    
            
    def ParseTarget(self, vals, return_list: list = []) -> list:
        """ Target Parser
        
        This is limited to scheme, hostname, and path only. 
        This will parse the url into three objects and return
        it base on what the user wants to return
        """
        
        url = urlparse(vals)

        scheme: str = url.scheme
        hostname: str = url.hostname
        path: str = url.path
        params: str = url.params
        query: str = url.query
        fragment: str = url.query
        username: str = url.username
        password: str = url.password
        port: int = url.port
        
        out: list = []

        for i in return_list:
            if i.lower() == 'scheme':
                out.append(scheme)
            if i.lower() == 'hostname':
                out.append(hostname)
            if i.lower() == 'path':
                out.append(path)
            if i.lower() == 'params':
                out.append(params)
            if i.lower() == 'query':
                out.append(query)
            if i.lower() == 'fragment':
                out.append(fragment)
            if i.lower() == 'username':
                out.append(username)
            if i.lower() == 'password':
                out.append(password)
            if i.lower() == 'port':
                out.append(port)
            else:
                pass
        return out

        
    def RandomName(self) -> str:
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