#######
# Util: Non-interactive Opt
#######

class noninteractive:
    ''' Interactive Option Usage
    
    :return: -> dict
    '''
    def options() -> dict:
        return {
            'Console options:': [
                {
                    '-c  --console-info': 'Display console information.'
                    },
                {
                    '-h, -H, --help': 'Display help banner.'
                    },
                {
                    '-s, --search-module WORD': 'Search and Display specific modules.'
                    },
                {
                    '-S, --show-all-module': 'Display all modules.'
                    }
                ],
            'Module options:': [
                {
                    '-m, --module-info PATH': 'Display the information of the module including options.'
                    },
                {
                    '-o, -opt, --show-options PATH': 'Display the module options.'
                    },
                {
                    '-u, --use-module PATH OPTIONS=VALUE': 'Runs the module in non-interactive mode.'
                    }
                ],
            'Framework options:': [
                {
                    '-v, -V, --version': 'Display the framework version.'
                    },
                {
                    '-l, -L, --license': 'Display the framework license.'
                    }
            ]
        }