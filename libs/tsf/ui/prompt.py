#######
# UI: Prompt
#######

from libs.tsf.ui.termcolor import s, f
from config.module_config import directories

def prompt(args) -> str:
    """ Generates prompt template for console command prompt """
    
    user, prompt, path = args
    if path != None:
        element = directories.get()
        try:
            module_type = [x for x in element if x in path][0]
            module_path = '(unknown module)' if not module_type[0] else path.replace(f"modules/{module_type}/",'') 
            module_template = ( 
                f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
                f'{module_type}(\001{s.BRIGHT}\002\001{f.RED}\002{module_path}\001{s.RESET_ALL}\002)' + ' ' + 
                f'{prompt}' + ' '
            )
            return module_template
            
        except:
            alternative_template = (
                f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
                f'[\001{f.CYAN}\002unknown\001{f.RESET}\002](\001{s.BRIGHT}\002\001{f.RED}\002{path}\001{s.RESET_ALL}\002)' + ' ' + 
                f'{prompt}' + ' '
            )
            return alternative_template
        
    else:
        default_template = (
            f'\001{s.UNDERLINE}\002{user}\001{s.RESET_ALL}\002' + ' ' +
            f'{prompt}' + ' '
        )
        return default_template