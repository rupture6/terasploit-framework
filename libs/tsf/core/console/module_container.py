# OBJECT MODULE
# SET MODULE
class Module(object):
    def __init__(self, module, path):
        self.module = module
        self.path = path
    def __get__(self, instance, owner):
        return self.module, self.path
    

class set_module(Module):
    def __set__(self, instance, value):
        self.module, self.path = value

# OBJECT ENCODER
# SET ENCODER
class Encoder(object):
    def __init__(self, encoder, path):
        self.encoder = encoder
        self.path = path
    def __get__(self, instance, owner):
        return self.encoder, self.path
    
class set_encoder(Encoder):
    def __set__(self, instance, value):
        self.encoder, self.path = value

# OBJECT PAYLOAD
# SET PAYLOAD
class Payload(object):
    def __init__(self, payload, path):
        self.payload = payload
        self.path = path
    def __get__(self, instance, owner):
        return self.payload, self.path
    
class set_payload(Payload):
    def __set__(self, instance, value):
        self.payload, self.path = value
   
# OBJECT DEFAULT PAYLOAD
# SET MODULE DEFAULT PAYLOAD     
class DefaultPayload(object):
    def __init__(self, path):
        self.default = path
    def __get__(self, instance, owner):
        return self.default
        
class set_module_default_payload(DefaultPayload):
    def __set__(self, instance, value):
        self.default = value