#######
# Util: Command Usage 
#######

class usage_banner:
    def info_usage() -> dict:
        return {
            'Usage: info [path]': [
            "  The 'Info' command displays the full information of the module."
            ],
            'Example:': [
                '  info auxiliary/scanner/http/domain/sub_domain_discovery'
                ]
            }
    
    def use_usage() -> dict:
        return {
            'Usage: use [path]': [
                "  The 'Use' command imports the module, allowing the user",
                '  to interact with the module and perform its task.'
                ],
            'Example:': [
                '  use exploit/http/xampp/windows/webdav_upload_php'
                ]
            }
    
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