#######
# Command: Help
#######

from init.teralib.util import Help
from init.teralib.ui import Table

# Command class

class _help_:
    
    @staticmethod
    def function() -> None:
        Core, Module = Help()
        Table.help_table(Core,Module)