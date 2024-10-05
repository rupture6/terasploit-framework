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
import multiprocessing

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
from init.teralib.ui import (
    print_info,
    f,
    b,
    s,
    clean_last_line
)

from init.teralib.core import Get
from init.teralib.base import Search
from libs.terasploit.framework.formatter.fix_data_type import DataType
from libs.terasploit.framework.opts.opt_distributor import Opt

from libs.terasploit.framework.clients.util.error_codes import (
    tcp_error_codes,
    udp_error_codes
)
from init.framework import (
    Shell,
    AddrFam,
    SockType,
    HTTP,
    TCPClient,
    UDPClient,
    SOCKClient
)
from libs.terasploit.framework.module.datastore import (
    Module,
    Extension,
    Arch,
    PayloadHandler,
    Platform
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
    'multiprocessing',
    
    # Exploit
    'Shell',
    
    # Data Handler
    'DataHandler',
    
    # UI 
    'print_info',
    'clean_last_line',
    'f',
    'b',
    's',
    
    # Base
    'Search',
    
    # Core
    'Get',
    
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
    'TCPClient',
    'UDPClient',
    'SOCKClient'
]