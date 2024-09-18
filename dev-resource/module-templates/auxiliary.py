#######
# Module/Auxiliary: Module Name
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitAuxiliary(Auxiliary):

    module_type = 'auxiliary'

    def initialize(self, info_only: bool = False):
        update_info (
            {
                'Module' : '',
                'Name' : '',
                'Author' : 'Handler4'
            }
        )
        
        register_option ("auxiliary",opt=[
            OptIP.new("lhost",[
                "","yes","target listening address"
            ]),
            OptPort.new("lport",[
                4444,"yes","target listening port"
            ])
        ])
        
    def run(self):
        pass
