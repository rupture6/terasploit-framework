#######
# Data: Data Handler
#######

import os
    
class DataHandler:
    
    def GetPath(path) -> str:
        """ Returns the path of the resource file 
        
        >>> self.GetResource('data/wordlist/admin/wordlist_adminpanel.txt')
        """
        
        return f"{os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))}/{path}"
