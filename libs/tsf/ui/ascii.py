#######
# UI: Ascii
#######

from libs.tsf.ui.termcolor import *

class ascii_banners:
    ''' Contains ascii banner arts for the console '''
    
    def contents() -> list[str]:
        # Banner 1
        B1 = s.BRIGHT + f.BLUE + '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
    ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁ ⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
    ⠀⠸⠟⠋ ⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆        ⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿    
    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
             ⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁          ⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟       
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
                    ⠈⢿⣿⣿⣿⣿⣿⣿⠟        ⢸⣿⣿⣿⣿⣷⢀⡄       ⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
                      ⢹⣿⣿⣿⣿⠟         ⠘⣿⣿⣿⣿⠉⣿⠃           ⣤⣾⣿⣿⣿⣿⣆ ⠰⠄⠀⠉⠀⠀
                      ⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃              ⢻⣿⠿⠿⣿⣿⣿⠇  ⢀    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''' + s.RESET_ALL + f.RESET

        # Banner 2
        B2 = s.BRIGHT + f.RED + '''
     ________  ________  ___    ___ ________      
    |\   ____\|\   __  \|\  \  /  /|\_____  \     
    \ \  \___|\ \  \|\  \ \  \/  / ||____|\  \    
     \ \_____  \ \   ____\ \    / /      \ \__\   
      \|____|\  \ \  \___|\/   / /        \|__|   
        ____\_\  \ \__\ __/   / /              ___ 
       |\_________\|__||\____/ /              |\__\ 
       \|_________|    \|____|/               \|__|

''' + s.RESET_ALL + f.RESET

        # Banner 3
        B3 = s.BRIGHT + '''  
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

        # Banner 4
        B4 = f.GREEN + '''
   ⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
    ⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
     ⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
  ⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
  ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
  ⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀
                       root@terasploit:~#
''' + f.RESET
        
        # Banner 5
        B5 = f"""{f.GREEN}
     _____              _____       _       _ _   
    |_   _|            /  ___|     | |     (_) |  
      | | ___ _ __ __ _\ `--. _ __ | | ___  _| |_ 
      | |/ _ \ '__/ _` |`--. \ '_ \| |/ _ \| | __|
      | |  __/ | | (_| /\__/ / |_) | | (_) | | |_ 
      \_/\___|_|  \__,_\____/| .__/|_|\___/|_|\__|
                             | |  {f.RESET}Framework{f.GREEN}     
                             |_|                  
{f.RESET}"""

        # Banner 6
        B6 = f"""{s.BRIGHT}{f.RED}
                  ..............
             ...asdasdawdaswaewsda...
       a...xzxklvznlkzxnkzlkmvzlxzdlkdsa...p
       aawlskdnlasndlawldlasdlkawlndalnslcgk
       'cxzmzlkx{f.RESET}TTTTT{f.RED}dkexploit{f.RESET}TTTTT{f.RED}trppaflg'
        zxczlxm{f.RESET}TTTTTTT.{f.RED}lkaam{f.RESET}.TTTTTTT{f.RED}sdgmakc
        xcvlmv{f.RESET}TTT`{f.RED}as{f.RESET}TTTT...TTTT{f.RED}bn{f.RESET}`TTT{f.RED}askmda
        cbvlmk{f.RESET}TTT{f.RED}dsads{f.RESET}TTTTTTT{f.RED}dbfkd{f.RESET}TTT{f.RED}askdma
        bvgkck{f.RESET}TTT{f.RED}lkxamn{f.RESET}`TTT`{f.RED}aslkas{f.RESET}TTT{f.RED}xcvlxa
        cvbkgmf{f.RESET}`T{f.RED}laksmcn{f.RESET}TTT{f.RED}askncla{f.RESET}T'{f.RED}xcvklpa
        ˙dfkencoderalabf{f.RESET}TTT{f.RED}sadklncalsndals˙
         ˙sadkmalsknfjas{f.RESET}TTT{f.RED}meakdlasmklcna˙
          ˙xcvkmxlkckdnd{f.RESET}TTT{f.RED}askmcaosklmar˙
           ˙yfklblxddkkm{f.RESET}'T'{f.RED}fxvcdrgklfdd˙
             ˙asauxiliaryasljfnasjnla˙
               ˙˙asjcadkfbzfckndl˙˙
                   ˙˙asddsadas˙˙
                       ˙˙a˙˙
{f.RESET}{s.RESET_ALL}"""
        
        return [
            B1, # Banner 1
            B2, # Banner 2
            B3, # Banner 3
            B4, # Banner 4
            B5, # Banner 5
            B6, # Banner 6
        ]
        