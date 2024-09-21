#######
# Module: Payload
#######

from __future__ import annotations
from libs.terasploit.framework.module.dependencies import *


class Payload(object):
    """ Payload Class """
    
    def generate_file(self,file_name,architecture,code) -> None:
        extension = getattr(ArchExtension,f'{architecture.upper()}')

        with open(f"{file_name}.{extension}", 'w') as shell:
            shell.write(code)