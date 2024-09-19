#######
# UI: Table
#######

import sys; sys.dont_write_bytecode = True
import os

from config.module_config import modules
from libs.tsf.ui.printer import info_print, print_overlap
from libs.tsf.ui.termline import *
from libs.tsf.ui.termcolor import *


class Util:
    """ Table Utilities Class"""
    
    def get_longest_obj(obj) -> int:
        """ Returns longest object length in int """
        return len(max(obj, key=len))
    
    
    def get_metadata_contents(path):
        """ Returns module metadata base on module type """
        
        auxiliary, encoder, exploit, payload = modules.get()
        if 'auxiliary' in path:
            return auxiliary
        if 'encoder' in path:
            return encoder
        if 'exploit' in path:
            return exploit
        if 'payload' in path:
            return payload
        

class Table:
    """ Table Class - Handles all table print in the console """
    

    def global_option(name, value, description) -> None:
        """ Display all curent available global options in tabled format """
        
        vals = [i.replace('modules/','') if i != 'None' else '' for i in value]
        
        nl = Util.get_longest_obj(name) + 2
        sl = Util.get_longest_obj(vals) + 1
        tl = os.get_terminal_size()[0]
        
        print (f'{line_feed()}Global Options')
        print (f'=============={line_feed()}')
        print (f"   {'Options'.ljust(nl):<9} {'Current Setting'.ljust(sl):<17} {'Description'}")
        print (f"   {'───────'.ljust(nl):<9} {'───────────────'.ljust(sl):<17} {'───────────'}")
        
        for x, y, z in zip(name,vals,description):
            content = (f"   {x.upper().ljust(nl):<9} {y.lower().ljust(sl):<17} {z.lower()}")
            count = len(content) - len(z)
            print (content[:tl])
            if content[tl:]:
                print_overlap(content,count)
        line_break()


    def module_option(option_type, path, name, value, required, description) -> None:
        """ Display all current available option of a module or payload in tabled format """
        
        vals = [str(x) for x in value]
        
        nl = Util.get_longest_obj(name) + 2
        sl = Util.get_longest_obj(vals) + 1
        tl = os.get_terminal_size()[0]
        
        print (f"{line_feed()}{option_type} options ({path.replace('modules/','')}):{line_feed()}")
        print (f"   {'Name'.ljust(nl):<6} {'Current Settings'.ljust(sl):<17} {'Required':<9} {'Description'}")
        print (f"   {'────'.ljust(nl):<6} {'────────────────'.ljust(sl):<17} {'────────':<9} {'───────────'}")
        
        for w, x, y, z in zip(name, vals, required, description):
            content = (f"   {w.upper().ljust(nl) :<6} {x.ljust(sl) :<17} {y:<9} {z}")
            count = len(content) - len(z)
            print (content[:tl])
            if content[tl:]:
                print_overlap(content,count)
        line_break()


    def all_module(result) -> None:
        """ Displays all current module available in tabled format """

        module_count = {
            'Exploit':len([x for x in result if 'exploit' in x]),
            'Auxiliary':len([x for x in result if 'auxiliary' in x]),
            'Payload':len([x for x in result if 'payload' in x]),
            'Encoder':len([x for x in result if 'encoder' in x])
        }
        unknown_module = {}
        
        sl = Util.get_longest_obj(result) + 1
        nl = Util.get_longest_obj(str(len(result)))
        tl = os.get_terminal_size()[0]
        
        for i in ['Encoder','Payload','Exploit','Auxiliary']:
            count = module_count[i]
            if count != 0:
                module_number = -1
                
                print (f"{line_feed()}{i}")
                print ('='*len(i) + f'{line_feed()}')
                print (f"   {'#'.ljust(nl):<3} {'Path'.ljust(sl):<17} {'Description'}")
                print (f"   {'─'.ljust(nl):<3} {'────'.ljust(sl):<17} {'───────────'}")
                for x in result:
                    try:
                        description = Util.get_metadata_contents(x)[x]['description']
                    except (TypeError,KeyError):
                        unknown_module[x] = 'Not found in module metadata.'
                        continue
                    if i.lower() in x:
                        module_number += 1
                        content = (f"   {str(module_number).ljust(nl):<3} {x.ljust(sl):<17} {description}")
                        count = len(content) - len(description)
                        print (content[:tl])
                        if content[tl:]:
                            print_overlap(content,count)
                line_break()
        
        if unknown_module:
            info_print ('Unknown module was found:',uplinebreak=True,downlinebreak=True)
            for path, desc in unknown_module.items():
                print (f" *  {s.UNDERLINE}{path}{s.RESET_ALL} - {desc}")
            line_break()
                
            
    def module(result,function_name,function_value) -> bool:
        """ Displays module search result in tabled format """
        
        if not result:
            info_print (f"Couldn't find anything related to '{function_value}'",type='RED')
            return False
        
        print (f'{line_feed()}{function_name} ({function_value}){line_feed()}')
        print (f"   {'#':<5} {'Path/Description'}")
        print (f"   {'─':<5} {'────────────────'}")
        
        name = s.BRIGHT + f.RED + function_value + f.RESET + s.RESET_ALL
        module_count = -1
        
        for x in result:
            try:
                description = Util.get_metadata_contents(x)[x]['description']
            except TypeError:
                description = 'No description available from modules metadata'
                continue
            module_count += 1
            path = x.replace(function_value,name)
            print (f"   {module_count :<5} {path:<17}")
            print (f"           {'└── '+description}{line_feed()}")
        return True
    
    
    def info_table(args) -> None:
        """ Displays info contents in arranged format. """
        
        for key, value in args:
            if isinstance(value,list):
                print (f"{line_feed()}{key}:{line_feed()}")
                for text in value:
                    if key.lower() == 'description':
                        print (f"  {text}")
                    else:
                        print (f"  - {text}")
                line_break()
            else:
                print (f"{key[:15].rjust(15)}  =>  {value}")
    

    def help_table(Core,Module) -> None:
        """ Displays help contents in tabled format """
        
        print (f'{line_feed()}Core Commands')
        print (f'============={line_feed()}')
        print (f"   {'Name'.ljust(17)} {'Description'}")
        print (f"   {'────'.ljust(17)} {'───────────'}")
        
        for key, value in Core.items():
            print (f'   {key[:17].ljust(17)} {value}')
        
        line_break()
        print (f'{line_feed()}Module Commands')
        print (f'==============={line_feed()}')
        print (f"   {'Name'.ljust(17)} {'Description'}")
        print (f"   {'────'.ljust(17)} {'───────────'}")
        
        for key, value in Module.items():
            print (f'   {key[:17].ljust(17)} {value}')
        print (line_feed())