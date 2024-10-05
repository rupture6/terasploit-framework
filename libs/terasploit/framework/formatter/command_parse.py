#######
# Formatter: Command Parse
#######

def parse_command(cmdline) -> tuple:
    """ Divides the command line into parts """
    
    args = []
    parsed = cmdline.strip().partition(' ')
    command, _, _ = parsed
    parameter, _, value = parsed[2].strip().partition(' ')
    
    if '--args:' in parameter or '--arg:' in parameter:
        args.append(parameter)
        parameter = ''
    
    if '--args:' in value or '--arg:' in value:
        args.append(value)
        value = ''
    
    return command, parameter, value, args