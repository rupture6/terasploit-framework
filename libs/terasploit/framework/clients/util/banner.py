#######
# Utils: Banner
#######

from __future__ import annotations
from init.teralib.ui import print_info

class Banner:
    
    @staticmethod
    def grab(sock,port: int) -> list|None:
        """ It uses GET http method and HTTP 1.1 to grab banner """
        
        try:
            banner = []
            if port == 80:
                sock.sendall("GET / HTTP/1.1\r\n\r\n")
                banner.append(sock.recv(4096))
            else:
                banner.append(sock.recv(4096))
            
            return banner
        
        except Exception as error:
            print_info (f'Banner grab error: {error}')