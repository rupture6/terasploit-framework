# Data storage via Python Descriptors

class Storage(object):
    """ Stores contents to be accessed by future functions """
    
    def __init__(self, content):
        self.content = content
        
    def __get__(self,instance,owner):
        return self.content
    
    
class storedata(Storage):
    """ Stores data into data storage """
    
    def __set__(self,instance,value):
        self.content = value