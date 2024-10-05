
import socket

from libs.terasploit.framework.clients.util.error_codes import (
    tcp_error_codes,
    udp_error_codes
)
from init.teralib.core import Logger
from init.teralib.ui import (
    f,
    print_info,
)

class SOCKClient:
    
    @staticmethod
    def GetPortServ(Port,Protocol):
        try:
            return socket.getservbyport(Port,Protocol)
        except:
            return 'Unknown'

    @staticmethod
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
                success_return = f'[{Host}] [{Port}:{proto}] [{banner}] [{f.GREEN}Open{f.RESET}]'
                Logger('info',success_return)
                print_info (success_return,type="GREEN")
                return True, success_return
            else:
                if Protocol.lower() == 'tcp':
                    tcp_error_return = f'[{Host}] [{Port}:{proto}] [{banner}] [{tcp_error_codes[connection]}]'
                    Logger('info',tcp_error_return)
                    print_info (tcp_error_return,type="RED")
                    return False, tcp_error_return
                if Protocol.lower() == 'udp':
                    udp_error_return = f'[{Host}] [{Port}:{proto}] [{banner}] [{udp_error_codes[connection]}]'
                    Logger('info',udp_error_return)
                    print_info (udp_error_return,type="RED")
                    return False, udp_error_return
                
        except Exception as error:
            exception_return = f'[{Host}] [{Port}:{proto}] [{banner}] [{error}]'
            Logger('error',exception_return)
            print_info (exception_return,type="RED")
            return False, exception_return