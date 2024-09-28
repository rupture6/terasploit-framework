#######
# Util: Help  Contents
#######

class Help:
    ''' Help
    
    :return: -> dict
    '''
    def contents() -> tuple[dict,dict]:

        Core: dict = {
            'banner' : 'Display banner',
            'set' : 'Inserts a value on the specified parameter',
            'show' : 'Displays information about the specified parameter',
            'unset' : 'Removes a value on the specified parameter',
            'options' : 'Display current module options available (shortcut command)',
            'search' : 'Finds a module by matching str characters from module path',
        }

        Module: dict = {
            'back' : 'Unuse the current module',
            'exploit' : 'Execute exploit module',
            'info' : 'Displays full module information',
            'run' : 'Execute non-exploit module',
            'use' : 'Interact with a module',
        }

        return Core, Module