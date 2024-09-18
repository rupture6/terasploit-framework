#######
# Utils: Sock
#######

import socket
import re
import logging

ipv4 = r"^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$"
ipv6 = r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

logger = logging.getLogger()

class ValidateIP:
    def is_ipv4(ip) -> bool:
        # credits: https://www.akto.io/
        flag_string = "gm"
        regex = re.compile(ipv4, sum(getattr(re, flag.upper()) for flag in flag_string if flag in "imsluxa"))
        return bool(regex.match(ip))

    def is_ipv6(ip) -> bool:
        # credits: https://ihateregex.io/
        flag_string = "gm"
        regex = re.compile(ipv6, sum(getattr(re, flag.upper()) for flag in flag_string if flag in "imsluxa"))
        return bool(regex.match(ip))

class GetSockFromIP:
    def __init__(self,ip,socket_type):
        self.ip = ip
        self.type = socket_type
        
    def return_content(self) -> socket:
        if ValidateIP.is_ipv4(self.ip):
            logger.info(f'Using socket for IPV4: {self.ip}')
            return socket.socket(socket.AF_INET, type=self.type)
        if ValidateIP.is_ipv6(self.ip):
            logger.info(f'Using scoket for IPV6: {self.ip}')
            return socket.socket(socket.AF_INET6, type=self.type)