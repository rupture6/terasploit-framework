#######
# Formatter: Command Parse
#######

class command_line:    
    
    def parse(args) -> tuple:
        parse_command = args.strip().partition(' ')
        parts = parse_command[2].strip().partition(' ')

        opts_key = []
        opts_value = []
        
        command = parse_command[0]
        if '-' in parts[0]:
            opts.append(parts[0])
        
        parameter = parts[0]    
        vals, _, _ = parts[2].strip().partition(' ')
        value = '' if '|' in vals else vals
        
        value_part = parts[2].split(' ')
        opts_list = value_part[1:] if '|' not in value_part[0] else value_part

        for i in opts_list:
            if '|' in i:
                opts_key.append(i)
            else:
                opts_value.append(i)
                
        opts = {}
        for key, val in zip(opts_key, opts_value):
            opts[key] = val

        return command, parameter, value, opts