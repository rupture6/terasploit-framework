#######
# Util: Console
#######

import sys

from libs.tsf.ui.termline import line_feed
from libs.tsf.ui.termcolor import f

class contents:
    """ Variables that are used in console for display """
    
    # Python version for banner.
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    # Interact message for successful module display.
    interact_message = f"{line_feed()}Interact with a module by its '{f.GREEN}path{f.RESET}' using '{f.GREEN}info{f.RESET}' or '{f.GREEN}use{f.RESET}' command. {line_feed()}"
    
    # Module info reminder 
    module_info = f"{line_feed()}{line_feed()}To view the full module information, use '{f.GREEN}info{f.RESET} <path>' command."

