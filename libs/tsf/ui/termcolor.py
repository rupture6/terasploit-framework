#######
# UI: Termcolor
#######

escape = '\x1b'

class f:
    """ Terminal Text Colors Class """
    
    BLACK   =   escape + '[30m'
    RED     =   escape + '[31m'
    GREEN   =   escape + '[32m'
    YELLOW  =   escape + '[33m'  
    BLUE    =   escape + '[34m'  
    MAGENTA =   escape + '[35m'  
    CYAN    =   escape + '[36m'  
    WHITE   =   escape + '[37m'  
    RESET   =   escape + '[39m'  


class b:
    """ Terminal Background Colors Class """
    
    BLACK   =   escape + '[40m'  
    RED     =   escape + '[41m'  
    GREEN   =   escape + '[42m'  
    YELLOW  =   escape + '[43m'  
    BLUE    =   escape + '[44m'  
    MAGENTA =   escape + '[45m'  
    CYAN    =   escape + '[46m'  
    WHITE   =   escape + '[47m'  
    RESET   =   escape + '[49m'  


class s:
    """ Terminal Style Colors Class """
    
    BRIGHT    =   escape + '[1m'  
    ITALIC    =   escape + '[3m'  
    DIM       =   escape + '[2m'  
    RESET_ALL =   escape + '[0m'  
    UNDERLINE =   escape + '[4m'  
    BLINK     =   escape + '[5m'  
    NEGATIVE  =   escape + '[7m'  
    CROSSED   =   escape + '[9m'  


class tb:
    """ Text Banner Class """
    
    YELLOW = s.BRIGHT + f.YELLOW + '[!]' + s.RESET_ALL
    RED    = s.BRIGHT + f.RED + '[-]' + s.RESET_ALL
    BLUE   = s.BRIGHT + f.BLUE + '[*]' + s.RESET_ALL
    GREEN  = s.BRIGHT + f.GREEN + '[+]' + s.RESET_ALL