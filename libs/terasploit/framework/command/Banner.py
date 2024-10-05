#######
# Command: Banner
#######

from init.teralib.base import Search
from libs.tsf.ui.banner import banner

# Command class

class _banner_:
    
    @staticmethod
    def function():
        modules = Search.all_modules()
        banner(modules)