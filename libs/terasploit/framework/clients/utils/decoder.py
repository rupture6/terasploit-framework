#######
# Utils: Decoder
#######

from __future__ import annotations
from init.tsf.ui.wildcard import info_print

class Decode:
    def content(client) -> str|any:
        buffer_size = 1024
        output = b''
        recv_len = 1
        
        while recv_len:
            try:
                data = client.recv(buffer_size)
                recv_len = len(data)
                output += data
                if recv_len < buffer_size:
                    break

            except Exception as error:
                info_print (error,type='red',downlinebreak=True)
                
        try:
            return output.decode('utf-8')
        except UnicodeDecodeError:
            return output.decode('latin-1')