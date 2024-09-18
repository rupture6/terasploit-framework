#######
# Functions
#######

import sys
import os
import traceback

from init.tsf.ui.wildcard import line_break, print_overlap, banner, clean_last_line, line_feed
from init.tsf.base.wildcard import Search

from libs.terasploit.framework.console import Loading
from libs.terasploit.framework.interpreter import base

options = {
    
    'Console options' : {
        '-h, --help' : 'Display this message',
        '-q, --quiet' : 'Starts the terasploit framework console without displaying the full banner',
        '--logs' : 'Enable console logging, it will log everything including command, error, info, and debug'
    },
    
    'Framework options' : {
        '-v, --version' : 'Shows the current version of the framework',
        '-l, --license' : 'Show the framework license'
    },
    
}

class Function(object):
    
    def minimal_banner(self) -> None:
        """ Displays the minimal banner """
        
        print ('Terasploit Framework :: Console :: Copyright (c) 2024, Rupture6')

    
    def opt(self) -> None:
        """ Displays full options """
        
        system = "Usage: terasploit [option]"
        simple = f"Usage: {sys.argv[0]} [option]"
        usage = system if '/usr/share' in sys.argv[0] else simple
        print (usage)
        
        tl = os.get_terminal_size()[0]
        for i in options:
            line_break()
            print (f"{i}:")
            for key, val in options[i].items():
                content = (f'   {key:<25}{val}')
                count = len(content) - len(val)
                print (content[:tl])
                if content[tl:]:
                    print_overlap(content,count)
    
    
    def startbase(self) -> None:
        """ Starts the base interpreter """
        
        try:
            with Loading(message='[*] Starting Terasploit Framework Console...'):
                from init import modules as _
            clean_last_line()
            
            modules = Search.all_modules()
            banner(modules)
            base.interpreter()
            
        except SystemExit:
            raise SystemExit
        except:
            lines = traceback.format_exc().splitlines()
            trace = traceback.format_tb(sys.exception().__traceback__)
            print (f'[*] Terasploit startup failed!')
            print (f'[*] {lines[0]}{line_feed()}')
            for i in trace:
                print (f"  --> {i}")
            print (f'[*] Error: {lines[-1]}')
            raise SystemExit
