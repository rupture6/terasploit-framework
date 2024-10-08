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
                'License'     : 'Terasploit Framework License (BSD)',
                'Module'      : Module.auxiliary,
                'Name'        : 'Hash Cracker',
                'Author'      : [
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
            OptFile.create('hash_file',['','yes','text file containing hashes line by line']),
            OptValidate.create('dictionary','wordlist',['','yes','the dictionary to use in hash cracking']),
            OptValidate.create('hash_type','cryptographic_hash',['sha-256','yes','the type of cryptographic hash to use']),
            OptString.create('salt',['','no','salt to use in hash cracking'])
        ])
        
        
    def run(self) -> None: 
        hash_file, dictionary, hash_type, salt = self.OPT()
        
        cryptographic_hash = hash_type.replace('-','')
        hashes = self.FormatFileContentsToList(hash_file)
        wordlist = self.FormatFileContentsToList(dictionary)
        
        print_info (f'Hashes: {str(len(hashes))}, Words: {str(len(wordlist))}')
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
                        print_info (f'Hash Cracked! - line {line} of {hash_file}',type='GREEN')
                        print (f' -  text: {text}')
                        print (f' -  digest: {digest}')
                        print (f' -  hexdigest: {hash_text}')
                        break 
            return 
        
        except Exception as error:
            print_info(error,type='RED')
            return