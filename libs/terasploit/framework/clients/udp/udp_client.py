#######
# Client: UDP Client
#######

from init.tsf.ui.wildcard import info_print
from libs.terasploit.framework.clients.utils.sock import GetSockFromIP
from init.tsf.core.wildcard import Logger

import socket


class UDPClient:
    def GetPortServ(Port):
        try:
            return socket.getservbyport(Port,'udp')
        except:
            return 'Unknown'
    
    def Bind(Host,Port) -> socket:
        proto = UDPClient.GetPortServ(Port)
        try:
            sock = GetSockFromIP(Host,socket.SOCK_DGRAM).return_content()
            sock.bind((Host,int(Port)))
            
            info_print (f'Listening on {Host}:{Port}')
            Logger('info',f'Listening on {Host}:{Port}')
            
            sock.listen(2) # For now, it is fixed at listen: 2
            connection, address = sock.accept()
            ip, port = address

            info_print(f"Connection received from {ip}:{port}")
            Logger('info',f"Connection received from {ip}:{port}")
            return connection

        except KeyboardInterrupt:
            print (f'{Host} {Port}/{proto} - Bind Interrupted')
            sock.close()
            return False
        except socket.error as error:
            info_print (f'{Host} {Port}/{proto} - {error}',type='red')
            return False
        except Exception as error:
            info_print (f'{Host} {Port}/{proto} - {error}',type='red')
            return False
    
    
    def Connect(Host,Port) -> socket:
        proto = UDPClient.GetPortServ(Port)
        try:
            info_print (f'Connecting on {Host}:{Port}')
            sock = GetSockFromIP(Host,socket.SOCK_STREAM)
            connection = sock.connect((Host,int(Port)))
            return connection

        except KeyboardInterrupt:
            print (f'{Host} {Port}/{proto} - Connect Interrupted')
            sock.close()
            return False
        except socket.error as error:
            info_print (f'{Host} {Port}/{proto} - {error}',type='red')
            return False
        except Exception as error:
            info_print (f'{Host} {Port}/{proto} - {error}',type='red')
            return False