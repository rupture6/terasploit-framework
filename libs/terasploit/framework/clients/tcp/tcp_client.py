#######
# Client: TCP Client
#######

import socket

from init.teralib.ui import print_info
from libs.terasploit.framework.clients.util.sock import GetSockFromIP
from libs.terasploit.framework.exploit.client import Session

class TCPClient:
    
    @staticmethod
    def Terminate(Host,Port) -> None:
        try:
            sock = GetSockFromIP(Host,socket.SOCK_STREAM).return_content()
            sock.connect((Host,int(Port)))
            sock.close()
        
        except Exception as error:
            print_info (f"tcpclient[terminate]: {error}",type='RED')
            sock.close()
            return
    
    
    @staticmethod
    def Bind(Host,Port) -> None:
        try:
            sock = GetSockFromIP(Host,socket.SOCK_STREAM).return_content()
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((Host,int(Port)))
            
            print_info (f'Listening on {Host}:{Port}')
            sock.listen(5)
                
            connection, address = sock.accept()

            setattr(Session,'received_connection',address)
            setattr(Session,'client',connection)
            return
        
        except Exception as error:
            print_info (f"tcpclient[bind]: {error}",type='RED')
            sock.close()
            return
        
    
    @staticmethod
    def Connect(Host,Port) -> None:
        try:
            sock = GetSockFromIP(Host,socket.SOCK_STREAM).return_content()
            sock.connect((Host,int(Port)))
            setattr(Session,'client',sock)
        
        except Exception as error:
            print_info (f"tcpclient[connect]: {error}",type='RED')
            sock.close()
            return