#######
# UI: Ascii
#######

from libs.tsf.ui.termcolor import s, f

def ascii_banners() -> list[str]:
    """ Returns ascii banner arts for the console """
    
    return [
        B1, # Banner 1
        B2, # Banner 2
        B3, # Banner 3
        B4, # Banner 4
    ]

B1 = s.BRIGHT + f.RED + '''
     ________  ________  ___    ___ ________      
    |\   ____\|\   __  \|\  \  /  /|\_____  \     
    \ \  \___|\ \  \|\  \ \  \/  / ||____|\  \    
     \ \_____  \ \   ____\ \    / /      \ \__\   
      \|____|\  \ \  \___|\/   / /        \|__|   
        ____\_\  \ \__\ __/   / /              ___ 
       |\_________\|__||\____/ /              |\__\ 
       \|_________|    \|____|/               \|__|

''' + s.RESET_ALL


B2 = s.BRIGHT + '''  
    Command > EXPLOIT DEVICE 127.0.0.1''' + f.RED + '''
    
    ERROR!
    
    01110101 01101110 01101011 01101110 01101111 01110111 01101110 
    01100011 01101111 01101101 01101101 01100001 01101110 01100100 
    48d23e58920c24c7263011e01fab2017
    0054a16bfd05077be3b138ccf2f523c89c66c4ae
    MDA1NGExNmJmZDA1MDc3YmUzYjEzOGNjZjJmNTIzYzg5YzY2YzRhZQ==
    f0ab31a24e9471543915115671539a0e5850bd072f0c0329a65e067a3fe2275a
    
    [''' + f.YELLOW + '!' + f.RED + ''']''' + f.RESET + ''' SOMETHING WENT WRONG.
''' + s.RESET_ALL + f.RESET


B3 = f.GREEN + """
     _____              _____       _       _ _   
    |_   _|            /  ___|     | |     (_) |  
      | | ___ _ __ __ _\ `--. _ __ | | ___  _| |_ 
      | |/ _ \ '__/ _` |`--. \ '_ \| |/ _ \| | __|
      | |  __/ | | (_| /\__/ / |_) | | (_) | | |_ 
      \_/\___|_|  \__,_\____/| .__/|_|\___/|_|\__|
                             | |  """ + f.RESET + 'Framework' + f.GREEN + """
                             |_|
""" + f.RESET
        
        
B4 = f"""
   ____________
  < {f.CYAN}terasploit{f.RESET} >
   ------------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\\
                  ||----w |
                  ||     || 

"""