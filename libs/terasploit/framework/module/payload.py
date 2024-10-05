#######
# Module: Payload
#######

from __future__ import annotations
from libs.terasploit.framework.module.dependencies import *


class PHP:
     # From metasploit php preamble
     start = "/*<?php /**/"
     
     # Normal php starter/ender
     begin = "<?php "
     end = " ?>"


class Payload(object):
    """ Payload Class """
    
    def generate_file(self,file_name,extension,code) -> None:
        """ Generates shell file """
        
        with open(f"{file_name}{extension}", 'w') as shell:
            shell.write(code)
        print_info ('File generated!')
        print_info(f'Saved as shell{extension}')
        
        
    def OPT(self):
        """ Returns the value of an option """
        
        opt_content = [x for x in Opt('payload').Get()[0]]
        out = [Opt('payload').GetOPT(x) for x in opt_content]

        return out