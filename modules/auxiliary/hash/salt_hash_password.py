#######
# Module/Auxiliary: Salt Hash Password
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
                'Name'        : 'Salt Hash Password',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Generates salted hash password'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary', opt=[
            OptString.new('password',['','yes','password to hash with salt']),
            OptString.new('salt',['','yes','the salt of the password']),
            OptValidate.new('hash_type','cryptographic_hash',['sha-256','yes','cryptographic hash to use'])
        ])


    def run(self):
        password, salt, hash_type = self.OPT()
        full_password = password + salt
        
        info_print ('Generating salted hash password...')
        try:
            cryptographic_hash = hash_type.replace('-','')
            cryptographic_function = getattr(self,f'hash_{cryptographic_hash}_')
            hexdigest, digest = cryptographic_function(full_password)
        
            print (f' -  password: {password}')
            print (f' -  salt: {salt}')
            print (f' -  pass/salt: {full_password}')
            print (f' -  digest: {digest}')
            print (f' -  hexdigest: {hexdigest}')
            
            return 'done', True
        
        except Exception as error:
            info_print (error,type='RED'),
            return 'exception', True