#######
# Command: Help
#######

from init.tsf.ui.wildcard import Table
from init.tsf.util.wildcard import Help

class _help_:
    
    def function() -> None:
        Core, Module = Help.contents()
        Table.help_table(Core,Module)