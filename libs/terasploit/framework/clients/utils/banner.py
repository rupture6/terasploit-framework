#######
# Utils: Banner
#######

from __future__ import annotations
from init.tsf.ui.wildcard import info_print

""" Banner Grabber

This will return receive data from socket.
"""

class Banner:
    def grab(sock,port: int) -> list|None:
        try:
            banner = []
            if port == 80:
                sock.sendall("GET / HTTP/1.1\r\n\r\n")
                banner.append(sock.recv(4096))
            else:
                banner.append(sock.recv(4096))
            
            return banner
        except Exception as error:
            info_print (f'Banner grab error: {error}')