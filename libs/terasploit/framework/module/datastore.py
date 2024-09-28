#######
# Framework: Data Store
#######    

# For encoder and payload
class Extension:
    """ File extensions (For Arch/Platform) """
    
    PHP = ".php"
    PYTHON = ".py"
    PERL = ".pl"
    
    
# For payload
class Arch:
    """ Payload Architectures """
    
    MULTI = ["php","python","perl","cmd"]
    PHP = "php"
    PYTHON = "python"
    PERL = "perl"
    CMD = "cmd"


# For payload
class Platform:
    """ Payload Platforms """
    
    MULTI = ["php","python","perl","cmd","windows","linux","unix"]
    PHP = "php"
    PYTHON = "python"
    PERL = "perl"
    CMD = "cmd"
    WINDOWS = "windows"
    LINUX = "linux"
    UNIX = "unix"
    OSX = "osx"
    

# For payload
class PayloadHandler:
    """ Payload Handler """
    
    REVERSE_TCP = "reverse_tcp"
    REVERSE_UDP = "reverse_udp"
    BIND_TCP = "bind_tcp"
    BIND_UDP = "bind_udp"


# Module Type
class Module:
    """ Module Types """
    
    auxiliary = 'auxiliary'
    encoder = 'encoder'
    exploit = 'exploit'
    payload = 'payload'