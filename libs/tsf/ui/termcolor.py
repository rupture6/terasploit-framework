#######
# UI: Termcolor
#######

prefix = '\001'
suffix = '\002'
escape = '\033'

class f:
    """ Terminal Text Colors Class """
    
    BLACK   = prefix + escape + '[30m' + suffix
    RED     = prefix + escape + '[31m' + suffix
    GREEN   = prefix + escape + '[32m' + suffix
    YELLOW  = prefix + escape + '[33m' + suffix
    BLUE    = prefix + escape + '[34m' + suffix
    MAGENTA = prefix + escape + '[35m' + suffix
    CYAN    = prefix + escape + '[36m' + suffix
    WHITE   = prefix + escape + '[37m' + suffix
    RESET   = prefix + escape + '[39m' + suffix


class b:
    """ Terminal Background Colors Class """
    
    BLACK   = prefix + escape + '[40m' + suffix
    RED     = prefix + escape + '[41m' + suffix
    GREEN   = prefix + escape + '[42m' + suffix
    YELLOW  = prefix + escape + '[43m' + suffix
    BLUE    = prefix + escape + '[44m' + suffix
    MAGENTA = prefix + escape + '[45m' + suffix
    CYAN    = prefix + escape + '[46m' + suffix
    WHITE   = prefix + escape + '[47m' + suffix
    RESET   = prefix + escape + '[49m' + suffix


class s:
    """ Terminal Style Colors Class """
    
    BRIGHT    = prefix + escape + '[1m' + suffix
    ITALIC    = prefix + escape + '[3m' + suffix
    DIM       = prefix + escape + '[2m' + suffix
    RESET_ALL = prefix + escape + '[0m' + suffix
    UNDERLINE = prefix + escape + '[4m' + suffix
    BLINK     = prefix + escape + '[5m' + suffix
    NEGATIVE  = prefix + escape + '[7m' + suffix
    CROSSED   = prefix + escape + '[9m' + suffix


class tb:
    """ Text Banner Class """
    
    YELLOW = s.BRIGHT + f.YELLOW + '[!]' + s.RESET_ALL
    RED    = s.BRIGHT + f.RED + '[-]' + s.RESET_ALL
    BLUE   = s.BRIGHT + f.BLUE + '[*]' + s.RESET_ALL
    GREEN  = s.BRIGHT + f.GREEN + '[+]' + s.RESET_ALL