#######
# Command: Banner
#######

from init.tsf.base.wildcard import Search
from init.tsf.ui.wildcard import banner

class _banner_:
    
    def function():
        modules = Search.all_modules()
        banner(modules)