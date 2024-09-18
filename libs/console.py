#######
# Console
#######

from libs.functions import Function, base
from init.tsf.core.wildcard import Logs


class console(Function):
    """ Class for console function """
    
    def __init__(self,key,value,dictionary):
        self.dictionary = dictionary
        self.key = key
        self.value = value
        self.function()
    
    
    def function(self) -> None:
        if self.key.lower() in ['-h','--help']:
            self.minimal_banner()
            self.opt()
            
        if self.key.lower() in ['-q','--quiet']:
            if '--log' in self.dictionary:
                Logs().logs()
            base.interpreter()
            
        if self.key.lower() in ['--log']:
            Logs().logs()
            if '-q' in self.dictionary or '--quiet' in self.dictionary:
                base.interpreter()
                return
            self.startbase()