#######
# Base: Path
#######

class Paths:

    @staticmethod
    def pythonize_path(args) -> any:
        """ Replaces / into . to make it a module path """
        
        return args.replace('/','.')
    

    @staticmethod
    def humanize_path(args) -> any:
        """ Replaces . into / to humanize the path (human readable path) """
        
        return args.replace('.','/')


    @staticmethod
    def parse_path(args) -> list:
        """ Divides the path into pieces via / """
        
        divide_parts = args.split('/')
        return list(filter(None,divide_parts))


    @staticmethod
    def join_path(args) -> str:
        """ Make a whole path via joining list with / """
        
        return '/'.join(y for y in args)
    

    @staticmethod
    def process_path(args) -> str:
        """ Process the path turning it into a module path by adding modules/ """
        
        valid_word = ['modules','module']
        parse = Paths.parse_path(args)
        if parse[0] not in valid_word:
            parse.insert(0,'modules')
        if parse[0] != 'modules': 
            parse[0] = 'modules'
            
        return Paths.join_path(parse)