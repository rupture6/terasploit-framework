#######
# Module: Encoder
#######

from __future__ import annotations

import bcrypt
import argon2
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

from libs.terasploit.framework.opts.opt_distributor import Opt
from libs.terasploit.framework.arch_extensions import ArchExtension

from init.terasploit.framework.clients.wildcard import *
from init.tsf.ui.wildcard import info_print, f
from init.tsf.base.wildcard import Search

__all__ = [
    'Opt',
    'Encoder',
    'info_print',
    'f',
    'bcrypt',
    'argon2',
    'sha1',
    'sha224',
    'sha256',
    'sha384',
    'sha512',
    'md5',
    'b64encode',
    'hexlify'
]

class Encoder(object):
    
    def payload_path_list(self) -> list:
        module_list = Search.all_modules()
        payloads = []

        for module in module_list:
            if 'payload' in module:
                payloads.append(module)
        return payloads


    def generate_file(self,file_name,architecture,encoded_code) -> None:
        extension = getattr(ArchExtension,f'{architecture.upper()}')

        with open(f"{file_name}.{extension}", 'w') as shell:
            shell.write(encoded_code)