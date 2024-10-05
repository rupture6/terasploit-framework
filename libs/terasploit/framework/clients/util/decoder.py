#######
# Utils: Decoder
#######

from __future__ import annotations
from init.teralib.ui import print_info

def Decode(client) -> str|any:
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
            print_info (error,type='red',downlinebreak=True)
                
    try:
        return output.decode('utf-8')
    except UnicodeDecodeError:
        return output.decode('latin-1')