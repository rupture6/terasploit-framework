#######
# UI: Banner
#######

from libs.terasploit import framework_info
from libs.tsf.ui.ascii import ascii_banners
from libs.tsf.util.console import contents
from libs.tsf.ui.termcolor import f
from libs.tsf.ui.termline import line_break
import random


class banner:
    def __init__(self,module_list):
        """ Starting point of the console_banner class """

        self.framework = framework_info.information()
        self.terasploit = f.YELLOW + 'terasploit' + ' ' + self.framework['framework-version'] + f.RESET
        self.module_list = module_list
        self.upper_banner()
        self.lower_banner()


    def upper_banner(self) -> None:
        """ Displays banner arts from TerasploitBanners class """
        
        print (random.choice(ascii_banners.contents()))


    def lower_banner(self) -> None:
        """ Displays the lower part of the banner """
        
        modules = self.module_list
        
        exploit_count = len([x for x in modules if 'exploit' in x])
        auxiliary_count = len([x for x in modules if 'auxiliary' in x])
        payload_count = len([x for x in modules if 'payload' in x])
        encoder_count = len([x for x in modules if 'encoder' in x])
        
        row_1 = f'exploit: {exploit_count}, auxiliary: {auxiliary_count}, payload: {payload_count}'
        row_2 = f'encoder: {encoder_count}'

        line_break()
        print (f"         =[ {self.terasploit[:56]:<56} ]")
        print (f'< -- + --=[ running in python - {contents.python_version[:26]:<26} ]')
        print (f"< -- + --=[ {row_1[:46]:<46} ]")
        print (f'< -- + --=[ {row_2[:46]:<46} ]')
        line_break()
        print (f'Total modules available: {len(modules)}')
        line_break()