#######
# Module: Payload
#######

from __future__ import annotations

from libs.terasploit.framework.opts.opt_distributor import Opt
from libs.terasploit.framework.arch_extensions import ArchExtension

from init.terasploit.framework.clients.wildcard import *
from init.tsf.ui.wildcard import info_print

__all__ = [
    'Opt',
    'Payload',
    'info_print'
]

class Payload(object):
    
    def generate_file(self,file_name,architecture,code) -> None:
        extension = getattr(ArchExtension,f'{architecture.upper()}')

        with open(f"{file_name}.{extension}", 'w') as shell:
            shell.write(code)