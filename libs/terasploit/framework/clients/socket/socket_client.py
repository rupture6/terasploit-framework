import socket
import logging

from libs.terasploit.framework.clients.utils.error_codes import tcp_error_codes, udp_error_codes
from init.tsf.ui.wildcard import f

logger = logging.getLogger()

class SOCKClient:
    def GetPortServ(Port,Protocol):
        try:
            return socket.getservbyport(Port,Protocol)
        except:
            return 'Unknown'

    def Connect_Ex(Sock,Host,Port,Timeout,Protocol) -> bool:
        """ Connect_Ex
        
        Instead of returning socket connection, this will return codes
        that will indicate whether a socket connection with port is 
        successful or not.
        """
        
        proto = SOCKClient.GetPortServ(Port,Protocol)
        try:
            sock = Sock
            socket.setdefaulttimeout(Timeout)
            connection = sock.connect_ex((Host,int(Port)))
            try:
                banner = Sock.recv(1024).strip().decode()
                if not banner:
                    banner = None
            except:
                banner = None
                
            sock.close()
            if connection == 0:
                success_return = f'{Host} {Port}/{proto} - {banner} - {f.GREEN}Open{f.RESET}'
                logger.info(success_return)
                print (success_return)
                return True, success_return
            else:
                if Protocol.lower() == 'tcp':
                    tcp_error_return = f'{Host} {Port}/{proto} - {banner} - {tcp_error_codes[connection]}'
                    logger.info(tcp_error_return)
                    print (tcp_error_return)
                    return False, tcp_error_return
                if Protocol.lower() == 'udp':
                    udp_error_return = f'{Host} {Port}/{proto} - {banner} - {udp_error_codes[connection]}'
                    logger.info(udp_error_return)
                    print (udp_error_return)
                    return False, udp_error_return
                
        except Exception as error:
            exception_return = f'{Host} {Port}/{proto} - {banner} - {error} - Exception Error'
            logger.info(exception_return)
            print (exception_return)
            return False, exception_return