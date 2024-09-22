#######
# Module/Auxiliary: Hash Cracker
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):

    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : Module.auxiliary,
                'Name'   : 'Hash Cracker',
                'Author'  : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Cracks hashes via Dictionary Attack, it cracks hashes',
                    'by matching encrypted objects (hash == dictionary).'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptFile.new('hash_file',['','yes','text file containing hashes line by line']),
            OptValidate.new('dictionary','wordlist',['','yes','the dictionary to use in hash cracking']),
            OptValidate.new('hash_type','cryptographic_hash',['sha-256','yes','the type of cryptographic hash to use']),
            OptString.new('salt',['','no','salt to use in hash cracking'])
        ])
        
        
    def run(self):
        hash_file, dictionary, hash_type, salt = self.OPT()
        
        cryptographic_hash = hash_type.replace('-','')
        hashes = self.FormatFileContentsToList(hash_file)
        wordlist = self.FormatFileContentsToList(dictionary)
        
        info_print (f'Hashes: {str(len(hashes))}, Words: {str(len(wordlist))}')
        try:
            line = 0
            for hash_text in hashes:
                line += 1
                for word in wordlist:
                    if salt:
                        text = word + salt
                    if not salt:
                        text = word
                        
                    cryptographic_function = getattr(self,f'hash_{cryptographic_hash}_')
                    hexdigest, digest = cryptographic_function(text)
                    if hexdigest in hash_text:
                        info_print (f'Hash Cracked! - line {line} of {hash_file}',type='GREEN')
                        print (f'  - text: {text}')
                        print (f'  - digest: {digest}')
                        print (f'  - hexdigest: {hash_text}')
                        break
                    
            return 'done', True
        
        except Exception as error:
            info_print(error,type='RED')
            return 'exception', True