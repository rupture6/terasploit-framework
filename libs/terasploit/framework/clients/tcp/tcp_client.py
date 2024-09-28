#######
# Client: TCP Client
#######

from init.tsf.ui.wildcard import info_print
from libs.terasploit.framework.clients.utils.sock import GetSockFromIP
from init.tsf.core.wildcard import Logger

import socket

class TCPClient:
    def GetPortServ(Port):
        try:
            return socket.getservbyport(Port,'tcp')
        except:
            return 'Unknown'
    
    def Bind(Host,Port) -> socket:
        proto = TCPClient.GetPortServ(Port)
        try:
            sock = GetSockFromIP(Host,socket.SOCK_STREAM).return_content()
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            sock.bind((Host,int(Port)))
            
            info_print (f'Listening on {Host}:{Port}')
            Logger('info',f'Listening on {Host}:{Port}')
            
            sock.listen(5)
            connection, address = sock.accept()
            ip, port = address

            info_print(f"Connection received from {ip}:{port}")
            Logger('info',f"Connection received from {ip}:{port}")
            return connection
        
        except KeyboardInterrupt:
            info_print ('Bind interrupted')
            sock.close()
            return False
        except socket.error as error:
            info_print (f'[{Host}] [{Port}:{proto}] [{error}]',type='red')
            sock.close()
            return False
        except Exception as error:
            info_print (error,type='red')
            sock.close()
            return False
    
    
    def Connect(Host,Port) -> socket:
        proto = TCPClient.GetPortServ(Port)
        try:
            info_print (f'Connecting on {Host}:{Port}')
            sock = GetSockFromIP(Host,socket.SOCK_STREAM)
            connection = sock.connect((Host,int(Port)))
            return connection
        
        except KeyboardInterrupt:
            info_print ('Bind interrupted')
            sock.close()
            return False
        except socket.error as error:
            info_print (f'[{Host}] [{Port}:{proto}] [{error}]',type='red')
            sock.close()
            return False
        except Exception as error:
            info_print (error,type='red')
            sock.close()
            return False