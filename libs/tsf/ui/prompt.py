#######
# UI: Prompt
#######

from config.module_config import directories
from itertools import dropwhile
from libs.tsf.ui.termcolor import *

class prompt:
    """ Generates prompt template for console command prompt """

    def generate_template(args) -> str:
        user, prompt, path = args
        if path != None:
            element = directories.get()
            split_path = path.split('/')
            remove_no_value = [x for x in split_path if x]
            shortened_path = list(dropwhile(lambda x: x not in element, remove_no_value))
            module = [x for x in shortened_path if x not in element]
            module_path = '/'.join(y for y in module[-2:])
            
            try: 
                module_template = (
                    f'{s.UNDERLINE}{user}{s.RESET_ALL}' + ' ' +
                    f'{shortened_path[0]}({s.BRIGHT}{f.RED}{module_path}{s.RESET_ALL})' + ' ' + 
                    f'{prompt}' + ' '   
                )
                return module_template
            
            except:
                alternative_template = (
                    f'{s.UNDERLINE}{user}{s.RESET_ALL}' + ' ' +
                    f'[unknown folder]({s.BRIGHT}{f.RED}{split_path[-1]}{s.RESET_ALL}{s.RESET_ALL})' + ' ' + 
                    f'{prompt}' + ' '
                )
                return alternative_template
        
        else:
            default_template = (
                f'{s.UNDERLINE}{user}{s.RESET_ALL}' + ' ' +
                f'{prompt}' + ' '
            )
            return default_template