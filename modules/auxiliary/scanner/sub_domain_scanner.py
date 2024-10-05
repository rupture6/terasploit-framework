#######
# Module/Auxiliary: Sub-Domain Scanner via HTTP Requests
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
                'Name'        : 'Sub-Domain Scanner via HTTP Requests',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Scans for sub-domain of the target via HTTP Requests.',
                ],
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptValidate.create('scheme','scheme',['http','yes','scheme of the url']),
            OptString.create('sub_domain',['','no','scan single sub-domain, remove value for mass scanning']),
            OptFile.create('sd_file',['','no','use custom sub-domain wordlist text']),
            OptString.create('sld',['google','yes','second-level domain of the url']),
            OptString.create('tld',['com','yes','top-level domain of the url or suffix']),
            OptValidate.create('timeout','timeout',[0.5,'yes','http connection timeout']),
            OptInt.create('threads',[3,'yes','max threads to use']),
            OptValidate.create('sleep','timeout',[5,'yes','threading sleep when max thread reached'])
        ])
    
    
    def httprequest(self,url,timeout) -> None:
        try:
            request = HTTP.Request('get', url=url, timeout=timeout)
            header = request.headers
            server = header.get('Server')
            if request.status_code in self.good_status_code():
                clean_last_line()
                self.successful_scan.append(f"[{url}] [server:{server}] [status:{request.status_code}]")
                print_info (f"[{url}] [server:{server}] [status:{request.status_code}]", type='green')
            else:
                clean_last_line()
                print_info (f"[{url}] [server:{server}] [status:{request.status_code}]", type='red')
                if request.status_code != 404:
                    self.failed_scan.append(f"[{url}] [server:{server}] [status:{request.status_code}]")
                if server:
                    self.failed_scan.append(f"[{url}] [server:{server}] [status:{request.status_code}]")
        except:
            pass
                
    def run(self) -> None:
        scheme, sub_domain, sd_file, sld, tld, timeout, threads, thread_sleep = self.OPT()
        
        target_sub_domain = []
        if not sd_file:
            path = self.GetData('data/wordlist/dns/wordlist_subdomain.txt')
            target_sub_domain = self.FormatFileContentsToList(path) if not sub_domain else list(sub_domain)
        else:
            target_sub_domain = self.FormatFileContentsToList(sd_file) if not sub_domain else list(sub_domain)

        try:
            max_threads = int(threads)
            for sd in target_sub_domain:    
                url = f'{scheme}://{sd}.{sld}.{tld}'
                while threading.active_count() > max_threads:
                    self.WarningPrint('Max threads reached! please wait...')
                    time.sleep(DataType.int_float_any(thread_sleep))
                    clean_last_line()
                    
                thread = threading.Thread(target=self.httprequest,args=[url,DataType.int_float_any(timeout)],daemon=True)
                thread.start()
        except KeyboardInterrupt:
            print ('Scanning interrupted, waiting for threads to finish before displaying result...')
            
        self.WaitThreads(thread)    
        print_info ('Sub-domains with bad response (filtered 404 with no server):')
        for i in self.failed_scan:
            print (f" -  {i}")
        print_info ('Sub-domains with good response:')
        for i in self.successful_scan:
            print (f" -  {i}")
            
        self.successful_scan.clear()
        self.failed_scan.clear()
        return 'done', True