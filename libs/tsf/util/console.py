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


class usage_banner:
    
    @staticmethod
    def info_usage() -> dict:
        return {
            'Usage: info [path]': [
            "  The 'Info' command displays the full information of the module."
            ],
            'Example:': [
                '  info exploit/multi/handler'
                ]
            }
    
    
    @staticmethod
    def use_usage() -> dict:
        return {
            'Usage: use [path]': [
                "  The 'Use' command imports the module, allowing the user",
                '  to interact with the module and perform its task.'
                ],
            'Example:': [
                '  use exploit/multi/handler'
                ]
            }
    
    
    @staticmethod
    def set_usage() -> dict:
        return {
            'Usage: (un)set [parameter] [value]': [
                "  'Set' command inserts a value in the selected",
                '  parameter. It validates the value first before',
                '  inserting it to avoid errors. The opposite of',
                "  this command is 'unset' which removes any value",
                '  from the parameter.'
                ],
            'Example:': [
                '  set lhost 127.0.0.1',
                '  unset lhost'
                ]
            }
        
        
    @staticmethod
    def unset_usage() -> dict:
        return {
            'Usage: (un)set [parameter] [value]': [
                "  'Set' command inserts a value in the selected",
                '  parameter. It validates the value first before',
                '  inserting it to avoid errors. The opposite of',
                "  this command is 'unset' which removes any value",
                '  from the parameter.'
                ],
            'Example:': [
                '  set lhost 127.0.0.1',
                '  unset lhost'
                ]
            }
            
            
    @staticmethod
    def show_usage() -> dict:
        return {
            'Usage: show [parameter]': [
                "  'Show' command displays the information or contents",
                '  of the specified parameter.'
                ],
            'Parameter:' : [
                '  all, options, auxiliary, encoder, exploit, payload'
                ],
            'Example:' : [
                '  show all'
                ]
            }
    
    
    @staticmethod
    def search_usage() -> dict:
        return {
            'Usage: search [dir|word]': [
                "  The 'Search' command will display a list of modules base on",
                '  what the word has matched on path list.'
                ],
            'Example:': [
                '  search exploit'
                ]
            }
        

def Help() -> tuple[dict,dict]:

    Core: dict = {
        'banner'  : 'Display banner',
        'set'     : 'Inserts a value on the specified parameter',
        'show'    : 'Display specified parameter contents',
        'unset'   : 'Removes a value on the specified parameter',
        'options' : 'Display current module options available (shortcut command)',
        'search'  : 'Finds a module by matching str characters from module path list',
    }

    Module: dict = {
        'back'    : 'Unuse the current module',
        'exploit' : 'Execute command for exploit module',
        'info'    : 'Display full module information',
        'run'     : 'Execute command for non-exploit module',
        'use'     : 'Interact with a module',
    }

    return Core, Module