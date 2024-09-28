#######
# Module/Auxiliary: XSS Query Inject via HTTP Requests
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'License'     : 'Terasploit Framework License (BSD)',
                'Module'      : Module.auxiliary,
                'Name'        : 'Banner Grabber',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Banner Grabber VIA Socket Library Of Python'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptValidate.new('rhost','host',['','yes','the remote host target (url/ip)']),
            OptPort.new('rport',[80,'yes','the target remote port']),
            OptInt.new('byte',[4096,'yes','bytes to receive from socket']),
            OptValidate.new('type','socket_type',['SOCK_STREAM','yes','socket type to specify']),
            OptValidate.new('family','address_family',['AF_INET','yes','address family to specify']),
            OptValidate.new('http_type','http_type',['HTTP/1.1','yes','type of http to use']),
            OptValidate.new('method','http_method',['HEAD','yes','http method to use']),
            OptValidate.new('timeout','timeout',[60,'yes','socket connection timeout'])  
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
        host, port, byte, socket_type, address_family, http_type, http_method, timeout = self.OPT()
        self.ParseURL(host)
        target = self.GetHostByName(Target.hostname)
    
        crlf = '\r\n'
        lf2 = '\n\n'
        crlf2 = crlf + crlf
        response_seperate = ''
        
        banner = None
        body = None
        
        info_print ('Grabbing banner...')
        try:
            sock = socket.socket(family=AddrFam.get(address_family),type=SockType.get(socket_type))
            sock.settimeout(DataType.int_float_any(timeout))
            sock.connect((target,int(port)))
        
            request_data = f"{http_method} / {http_type} {crlf}"
            if http_type == "HTTP/1.1":
                request_data += f'Host: {target}:{port}{crlf}'
                request_data += f"Connection: close{crlf}"
            request_data += crlf
        
            sock.sendall(request_data.encode())
            received_chunks = self.get_chunk(sock,int(byte))
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

            print (f'Host: {target}:{port}')
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