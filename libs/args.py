#######
# Args
#######

import sys

from libs.functions import Function
from libs.framework import framework
from libs.console import console
from libs.optdict import optdict

                
class Argv(Function):
    """ Terasploit argv interpreter class """
    
    def __init__(self) -> None:
        """ Starting point of the argpreter """

        self.args = sys.argv[1:]
        self.dictionary = {}
        
        self.Parser()
        self.Identifier()
        
        
    def Parser(self):
        """ Parse the argv contents """
        
        key = None
        for i in self.args:
            if '-' in i:
                key = i
            if not key:
                key = i
            self.dictionary[key] = i
            
            
    def Identifier(self):
        """ Identify where does the option belong """
        
        for key, val in self.dictionary.items():
            if key.lower() in optdict['console']:
                console(key,val,self.dictionary)
                return
            if key.lower() in optdict['framework']:
                framework(key,val,self.dictionary)
                return
            else:
                self.minimal_banner()
                print (f"Error: an invalid option was specified '{key}'")
                self.opt()
                return