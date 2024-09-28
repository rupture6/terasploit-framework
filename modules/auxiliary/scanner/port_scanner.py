#######
# Module/Auxiliary: Socket Open Port Scanner
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    successful_scan = []
    failed_scan = []
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'License'     : 'Terasploit Framework License (BSD)',
                'Module'      : Module.auxiliary,
                'Name'        : 'Open Port Scanner',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'This module is an advance threaded port scanner that allows',
                    'the user to scan for open ports in specific range of ports.'
                ],
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptValidate.new('rhost','host',['','yes','the remote host target (url/ip)']),
            OptValidate.new('port_range','port_range',['80-443','no','port range to scan, remove value to scan all port']),
            OptValidate.new('type','socket_type',['SOCK_STREAM','yes','socket type to specify']),
            OptValidate.new('family','address_family',['AF_INET','yes','address family to specify']),
            OptInt.new('threads',[3,'yes','max threads to use']),
            OptValidate.new('sleep','timeout',[5,'yes','threading sleep when max thread reached']),
            OptValidate.new('timeout','timeout',[0.5,'yes','socket connection timeout']),
            OptValidate.new('protocol','protocol',['tcp','yes','socket protocol to use'])
        ])

    
    def connect(self,sock,host,port,timeout,protocol) -> None:
        connection = SOCKClient.Connect_Ex(sock,host,port,timeout,protocol)
        boolean, connection_return = connection
        if boolean == True:
            self.successful_scan.append(connection_return)
        if boolean == False:
            self.failed_scan.append(connection_return)
    
    
    def run(self) -> tuple[str, bool]: 
        host, port_range, socket_type, address_family, threads, thread_sleep, timeout, protocol = self.OPT()
        self.ParseURL(host)
        target = self.GetHostByName(Target.hostname)
        
        r1, r2 = port_range.split('-')
        range1 = r1.strip(' ')
        range2 = r2.strip(' ')
        
        info_print ('Scanning for open ports...')
        try:
            max_threads = int(threads)
            for port in range(int(range1),int(range2) + 1):
                sock = socket.socket(family=AddrFam.get(address_family),type=SockType.get(socket_type))
                while threading.active_count() > max_threads:
                    self.WarningPrint('Max threads reached! please wait...')
                    time.sleep(DataType.int_float_any(thread_sleep))
                    clean_last_line()
                    
                thread = threading.Thread(target=self.connect,args=[sock,target,int(port),DataType.int_float_any(timeout),protocol],daemon=True)
                thread.start()
        except KeyboardInterrupt:
            print ('Scanning interrupted, waiting for threads to finish before displaying result...')
        
        self.WaitThreads(thread)
        info_print (f'Open Ports: {len(self.successful_scan)}')
        for i in self.successful_scan:
            print (f" -  {i}")
        info_print (f'Closed/Filtered Ports: {len(self.failed_scan)}')
        
        self.successful_scan.clear()
        self.failed_scan.clear()
        return 'done', True