#######
# Module/Payload: Generic Reverse TCP
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitPayload(Payload):
    
    def initialize(self,info_only: bool = False) -> None:
        update_info(
            {
                'License'        : 'Terasploit Framework License (BSD)',
                'Name'           : 'Shell Reverse TCP Generic',
                'PayloadHandler' : PayloadHandler.REVERSE_TCP,
                'Module'         : Module.payload,
                'Author'         : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description'    : [
                    'Connect back on the target machine'
                ],
                
            }
        )
        
        if info_only:
            return

        register_option ("payload",opt=[
            OptIP.create("lhost",["","yes","the listening address"]),
            OptPort.create("lport",[4444,"yes","the listening port (tcp)"])
        ])