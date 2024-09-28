#######
# Module/Auxiliary: Phone Number World Lookup
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
                'Name'        : 'Phone Number World Lookup',
                'Author'      : [
                    'Charlie <rupture6.dev[at]gmail.com>'
                ],
                'Description' : [
                    'Looks up the phone number if it exist in some country.',
                    'For existing number, it will display full information'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary', opt=[
            OptValidate.new('number','phone_number',['','yes','target phonenumber to lookup, do not put "+(cc)"'])
        ])
        
    
    number_type = {
        '0'  :  'fixed line',
        '1'  :  'mobile',
        '2'  :  'fixed line or mobile',
        '3'  :  'toll free',
        '4'  :  'premium rate',
        '5'  :  'shared cost',
        '6'  :  'voice over ip number - including (TSoIP)',
        '7'  :  'personal number',
        '8'  :  'pager',
        '9'  :  'universal access number / company number',
        '10' :  'voice mail access number',
        '99' :  'unknown'
    }


    def timezone_print(self,timezone) -> None:
        print (' -  Timezone')
        for i in timezone:
            current_utc = datetime.now(pytz.timezone('UTC'))
            number_timezone = current_utc.astimezone(pytz.timezone(i))
            print ('      └─────',i + ':',f.CYAN + str(number_timezone) + f.RESET)


    def length_of_geographical_area_code(self,phone) -> None:
        nsn = phonenumbers.national_significant_number(phone)
        ac_len = phonenumbers.length_of_geographical_area_code(phone)
        if ac_len > 0:
            area_code = nsn[:ac_len]
            subscriber_number = nsn[ac_len:]
        else:
            area_code = ""
            subscriber_number = nsn
        print (f' -  Geographical Area Code Length: {f.CYAN}{area_code}{f.RESET}')
        print (f' -  Subscriber Number: {f.CYAN}{subscriber_number}{f.RESET}')


    def length_of_national_destination_code(self,phone) -> None:
        nsn = phonenumbers.national_significant_number(phone)
        ndc_len = phonenumbers.length_of_national_destination_code(phone)
        if ndc_len > 0:
            national_destination_code = nsn[:ndc_len]
            subscriber_number = nsn[ndc_len:]
        else:
            national_destination_code = ""
            subscriber_number = nsn
        print (f' -  National Destination Code Length: {f.CYAN}{national_destination_code}{f.RESET}')
        print (f' -  Subscriber Number: {f.CYAN}{subscriber_number}{f.RESET}')      

        
    def run(self) -> tuple[str,bool]:
        number = self.OPT()[0]
        iso_file = self.GetData('data/wordlist/code/iso31661a2cc.txt')
        iso_codes = self.FormatFileContentsToList(iso_file)

        for codes in iso_codes:
            try:
                phone_number = phonenumbers.parse(number, codes)
                phone_validity = phonenumbers.is_valid_number(phone_number)
                if phone_validity:
                    info_print (f'Phone number found in {f.CYAN}{codes}{f.RESET}',type='GREEN')
                    
                    print (f' -  Country: {f.CYAN}{pycountry.countries.get(alpha_2=phone_country(str(phone_number.country_code)+str(phone_number.national_number))).name}{f.RESET}')
                    print (f' -  Location: {f.CYAN}{phonenumbers_geocoder.description_for_number(phone_number,"en")}{f.RESET}')
                    print (f' -  Carrier: {f.CYAN}{phonenumbers_carrier.name_for_number(phone_number,"en")}{f.RESET}')
                    print (f' -  National : {f.CYAN}{phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)}{f.RESET}')
                    print (f' -  International: {f.CYAN}{phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{f.RESET}')
                    print (f' -  E164: {f.CYAN}{phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)}{f.RESET}')
                    print (f' -  RFC3966: {f.CYAN}{phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.RFC3966)}{f.RESET}')
                    print (f' -  Number Type: {f.CYAN}{self.number_type[str(phonenumbers.phonenumberutil.number_type(phone_number))]}{f.RESET}')
                    print (f' -  Is Dialed Internationally: {f.CYAN}{phonenumbers.phonenumberutil.can_be_internationally_dialled(phone_number)}{f.RESET}')
                    
                    self.length_of_national_destination_code(phone_number)
                    self.length_of_geographical_area_code(phone_number)
                    self.timezone_print(phonenumbers_timezone.time_zones_for_number(phone_number))
                    
            except KeyboardInterrupt:
                print ('Interrupt: Module function was interrupted')
                break
            except Exception:
                continue
        
        return 'done', True