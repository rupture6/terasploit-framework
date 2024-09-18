#######
# Module/Auxiliary: Socket Open Port Scanner
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitAuxiliary(Auxiliary):
    
    module_type = 'auxiliary'
    successful_scan = []
    failed_scan = []
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : 'auxiliary',
                'Name' : 'Open Port Scanner',
                'Author' : 'Charlie (4steroth)',
                
                'Description' : [
                    'This module is an advance threaded port scanner that allows',
                    'the user to scan for open ports in specific range of ports.'
                ],
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptString.new('target','host',['','yes','target host to scan']),
            OptString.new('port_range','port_range',['80-443','no','port range to scan, remove value to scan all port']),
            OptString.new('type','socket_type',['SOCK_STREAM','yes','socket type to specify']),
            OptString.new('family','address_family',['AF_INET','yes','address family to specify']),
            OptInt.new('threads',[3,'yes','max threads to use']),
            OptString.new('sleep','timeout',[5,'yes','threading sleep when max thread reached']),
            OptString.new('timeout','timeout',[0.5,'yes','socket connection timeout']),
            OptString.new('protocol','protocol',['tcp','yes','socket protocol to use'])
        ])

    
    def connect(self,sock,host,port,timeout,protocol) -> None:
        connection = SOCKClient.Connect_Ex(sock,host,port,timeout,protocol)
        boolean, connection_return = connection
        if boolean == True:
            self.successful_scan.append(connection_return)
        if boolean == False:
            self.failed_scan.append(connection_return)
    
    
    def run(self) -> tuple[str, bool]: 
        host = self.GetOPT('target')
        port_range = self.GetOPT('port_range')
        socket_type = self.GetOPT('type')
        address_family = self.GetOPT('family')
        threads = self.GetOPT('threads')
        timeout = DataType.int_float_any(self.GetOPT('timeout'))
        protocol = self.GetOPT('protocol')
        thread_sleep = DataType.int_float_any(self.GetOPT('sleep'))
        
        hostname = self.ParseTarget(host,return_list=['hostname'])
        if not hostname[0]:
            target = host
        if hostname[0]:
            target = self.GetHostByName(hostname[0])
        
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
                    time.sleep(thread_sleep)
                    clean_last_line()
                    
                thread = threading.Thread(target=self.connect,args=[sock,target,int(port),timeout,protocol],daemon=True)
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