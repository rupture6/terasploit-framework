#######
# Util: Help  Contents
#######

class Help:
    ''' Help
    
    :return: -> dict
    '''
    def contents() -> tuple[dict,dict]:

        Core: dict = {
            'banner' : 'Display banner.',
            'set' : 'Inserts a value on the specified parameter.',
            'show' : 'Displays information about the specified parameter.',
            'unset' : 'Removes a value on the specified parameter',
        }

        Module: dict = {
            'back' : 'Unuse the current module.',
            'exploit' : 'Executes the current module in use.',
            'info' : 'Displays full module information.',
            'options' : 'Display current options available.',
            'run' : 'Execute a module.',
            'search' : 'Finds a module by matching str characters from module path.',
            'use' : 'Interact with a module.',
        }

        return Core, Module