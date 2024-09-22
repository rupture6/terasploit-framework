#######
# Framework
#######

from libs.functions import Function
from libs.terasploit.framework_info import information


class framework(Function):
    """ Class for framework function """
    
    def __init__(self,key,value,dictionary):
        self.dictionary = dictionary
        self.key = key
        self.value = value
        self.function()
    
    
    def function(self) -> None:
        if self.key.lower() in ['-v','--version']:
            self.version()
        if self.key.lower() in ['-l','--license']:
            self.license()
    
    
    def license(self) -> None:
        """ Shows framework license """
        
        print (f"Framework: {information()['framework-license']}")
    
    
    def version(self) -> None:
        """ Shows current framework version """
        
        print (f"Framework: {information()['framework-version']}")