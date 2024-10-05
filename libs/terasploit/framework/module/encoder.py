#######
# Module: Encoder
#######

from libs.terasploit.framework.module.dependencies import *

class Encoder(object):
    """ Encoder Class """
    
    def payload_path_list(self) -> list:
        module_list = Search.all_modules()
        payloads = []

        for module in module_list:
            if 'payload' in module:
                payloads.append(module)
        return payloads


    def generate_file(self,file_name,architecture,encoded_code) -> None:
        extension = getattr(Extension,f'{architecture.upper()}')

        with open(f"{file_name}{extension}", 'w') as shell:
            shell.write(encoded_code)