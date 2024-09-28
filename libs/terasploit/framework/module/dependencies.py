#######
# Module: Dependencies
#######

"""
Contains all the libraries required to run modules.

NOTE: The console will not run if some modules are not installed
"""

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
import json
import base64
import re
import phonenumbers
import pycountry
import pytz

from datetime import datetime
from phonenumbers import geocoder as phonenumbers_geocoder
from phonenumbers import carrier as phonenumbers_carrier
from phonenumbers import timezone as phonenumbers_timezone
from phone_iso3166.country import phone_country
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
from requests.auth import HTTPDigestAuth

from base64 import b64encode
from binascii import hexlify
from hashlib import (
    sha1,
    sha224,
    sha256,
    sha384,
    sha512,
    md5
)

from data.data_handler import DataHandler

from init.tsf.ui.wildcard import (
    info_print, 
    f, 
    b, 
    s, 
    clean_last_line
)

from init.tsf.base.wildcard import Search

from libs.terasploit.framework.exploit.aggregator import Shell
from libs.terasploit.framework.opts.opt_distributor import Opt
from libs.terasploit.framework.clients.utils.familiy_address import AddrFam
from libs.terasploit.framework.clients.utils.socket_kind import SockType

from libs.terasploit.framework.clients.utils.error_codes import (
    tcp_error_codes, 
    udp_error_codes
)

from libs.terasploit.framework.formatter.fix_data_type import DataType
from libs.terasploit.framework.module.datastore import (
    Module,
    Extension,
    Arch,
    PayloadHandler,
    Platform
)

from init.terasploit.framework.clients.wildcard import (
    HTTP,
    HTTPClient,
    TCPClient,
    UDPClient,
    SOCKClient
)

__all__ = [
    
    # Python Libraries
    'sys',
    'urllib3',
    'requests',
    'socket',
    'random',
    'string',
    'warnings',
    'threading',
    'time',
    'traceback',
    'yaml',
    'json',
    'base64',
    're',
    'urlparse',
    'BeautifulSoup',
    'MarkupResemblesLocatorWarning',
    'HTTPDigestAuth',
    'b64encode',
    'hexlify',
    'sha1',
    'sha224',
    'sha256',
    'sha384',
    'sha512',
    'md5',
    'phonenumbers',
    'phonenumbers_geocoder',
    'phonenumbers_carrier',
    'phonenumbers_timezone',
    'pycountry',
    'pytz',
    'phone_country',
    'datetime',
    
    # Data Handler
    'DataHandler',
    
    # UI 
    'info_print',
    'clean_last_line',
    'f',
    'b',
    's',
    
    # Base
    'Search',
    
    # Exploit
    'Shell',
    
    # Opts
    'Opt',
    
    # Clients Utils
    'AddrFam',
    'SockType',
    'tcp_error_codes',
    'udp_error_codes',
    
    # Formatter
    'DataType',

    # Module Data
    'Module',
    'Extension',
    'Arch',
    'PayloadHandler',
    'Platform',
    
    # Clients
    'HTTP',
    'HTTPClient',
    'TCPClient',
    'UDPClient',
    'SOCKClient'
]