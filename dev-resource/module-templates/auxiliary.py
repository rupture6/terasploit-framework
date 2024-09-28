#######
# Module/Auxiliary: Module Name
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'License'     : 'Terasploit Framework License (BSD)',
                'Name'        : ' -- module name -- ',
                'Module'      : Module.auxiliary,
                'Author'      : [
                    ' -- author --'
                ],
                'Description' : [
                    ' -- description of the module -- '
                ],
            }
        )

        if info_only:
            return

        register_option (module="auxiliary",reset=True)

    def run(self) -> tuple[str, bool]: 
        return 'done', True
