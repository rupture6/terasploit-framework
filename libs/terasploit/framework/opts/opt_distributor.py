#######
# Opts: Opt Distributor
#######

from libs.terasploit.framework.opts.opt_container import ModuleOpt

class Opt(ModuleOpt):
    """ Returns the current module options to be used 
    
    >>> Opt('exploit').Get()
    >>> Opt('exploit').GetOPT('host')
    """
    
    def __init__(self,module_type):
        """ init function to get module type for option retrieving """
        self.module_type = module_type


    def Get(self):
        """ returns the full dictionary options """
        
        return getattr(self,f"{self.module_type.lower()}_opt"), self.module_type
    
    
    def GetOPT(self, option_name: str):
        """ returns a value from specific module option """
        
        try:
            opt = getattr(self,f"{self.module_type.lower()}_opt")
            return opt[option_name][0][0]
        except:
            return None
    
