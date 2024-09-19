#######
# Module/Auxiliary: XSS Query Inject via HTTP Requests
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    module_type = 'auxiliary'

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : 'auxiliary',
                'Name' : 'Banner Grabber',
                'Author' : 'Charlie (4steroth)',

                'Description' : [
                    'Banner Grabber VIA Socket Library Of Python'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptString.new('target','host',['','yes','target host (ip/url)']),
            OptPort.new('rport',[80,'yes','target port']),
            OptString.new('byte','int',[4096,'yes','bytes to receive from socket']),
            OptString.new('type','socket_type',['SOCK_STREAM','yes','socket type to specify']),
            OptString.new('family','address_family',['AF_INET','yes','address family to specify']),
            OptString.new('http_type','http_type',['HTTP/1.1','yes','type of http to use']),
            OptString.new('method','http_method',['HEAD','yes','http method to use']),
            OptString.new('timeout','timeout',[60,'yes','socket connection timeout'])  
        ])
        
    
    def get_chunk(self,sock,byte) -> bytes:
        response_data = b''
        while True:
            try:
                chunk = sock.recv(byte)
                response_data += chunk
            except Exception as error:
                print (f'Error occured: {error}')
                break
            if not chunk:
                break
        return response_data
  
    
    def run(self) -> None:
        host = self.GetOPT('target')
        port = int(self.GetOPT('rport'))
        byte = int(self.GetOPT('byte'))
        socket_type = self.GetOPT('type')
        address_family = self.GetOPT('family')
        http_type = self.GetOPT('http_type').upper()
        http_method = self.GetOPT('method').upper()
        timeout = DataType.int_float_any(self.GetOPT('timeout'))
        
        hostname = self.ParseTarget(host,return_list=['hostname'])
        if not hostname[0]:
            target = host
        if hostname[0]:
            target = self.GetHostByName(hostname[0])
    
        crlf = '\r\n'
        lf2 = '\n\n'
        crlf2 = crlf + crlf
        response_seperate = ''
        
        banner = None
        body = None
        
        info_print ('Grabbing banner...')
        try:
            sock = socket.socket(family=AddrFam.get(address_family),type=SockType.get(socket_type))
            sock.settimeout(timeout)
            sock.connect((target,port))
        
            request_data = f"{http_method} / {http_type} {crlf}"
            if http_type == "HTTP/1.1":
                request_data += f'Host: {target}:{port}{crlf}'
                request_data += f"Connection: close{crlf}"
            request_data += crlf
        
            sock.sendall(request_data.encode())
            received_chunks = self.get_chunk(sock,byte)
            if received_chunks:
                response_data = received_chunks.decode()
                if crlf2 in response_data:
                    response_seperate = crlf2
                elif lf2 in response_data:
                    response_seperate = lf2                
            else:
                print (f"{target} {http_method} {http_type} - no response received")
                return
            if response_seperate not in [crlf2, lf2] or response_data.startswith('<'):
                body = response_data
            else:
                contents = response_data.split(response_seperate)
                banner, body = "".join(contents[:1]), "".join(contents[1:])

            print ('-- banner --')
            if not banner:
                print (None)
            if banner:
                print (banner)
            print ('-- body --')
            if not body:
                print (None)
            if body:
                print (body)
            return 'done', True
        
        except Exception as error:
            info_print (error,type='red',downlinebreak=True,uplinebreak=True)
            return 'exception', True