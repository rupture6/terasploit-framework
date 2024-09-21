#######
# UI: Prompt
#######

from config.module_config import directories
from itertools import dropwhile
from libs.tsf.ui.termcolor import s, f


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
                    f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
                    f'{shortened_path[0]}(\001{s.BRIGHT}\002\001{f.RED}\002{module_path}\001{s.RESET_ALL}\002)' + ' ' + 
                    f'{prompt}' + ' '
                )
                return module_template
            
            except:
                alternative_template = (
                    f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
                    f'[unknown folder](\001{s.BRIGHT}\002\001{f.RED}\002{split_path[-1]}\001{s.RESET_ALL}\002)' + ' ' + 
                    f'{prompt}' + ' '
                )
                return alternative_template
        
        else:
            default_template = (
                f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
                f'{prompt}' + ' '
            )
            return default_template