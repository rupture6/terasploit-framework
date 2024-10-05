class Module(object):
    def __init__(self, module, path):
        self.module = module
        self.path = path
    def __get__(self, instance, owner):
        return self.module, self.path
    

class set_module(Module):
    def __set__(self, instance, value):
        self.module, self.path = value


class Encoder(object):
    def __init__(self, encoder, path):
        self.encoder = encoder
        self.path = path
    def __get__(self, instance, owner):
        return self.encoder, self.path
    
    
class set_encoder(Encoder):
    def __set__(self, instance, value):
        self.encoder, self.path = value


class Payload(object):
    def __init__(self, payload, path):
        self.payload = payload
        self.path = path
    def __get__(self, instance, owner):
        return self.payload, self.path
    
    
class set_payload(Payload):
    def __set__(self, instance, value):
        self.payload, self.path = value