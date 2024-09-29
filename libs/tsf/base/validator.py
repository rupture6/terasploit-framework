#######
# Base: Validator
# 
# This class is mainly used in module options validation.
# It validates the set value before inserting it in
# the module options container.
#
# It has 2 base validators (passive) which is IP and URL, 
# it validates the value via regex patterns.
#
# Functions with 'validate' are the active validators
# of this class, those are the functions that is always 
# called whenever a user set a value from an option.
#
# Base validators or passive validators are only called
# by active validators that requires their function. It
# is not called by any other function outside the class.
#######

import re

class validator:
    def URL(value) -> bool:
        """ Base URL validator
        
        This wll validate url using django regex validator. 
        Source: https://github.com/django/django/blob/main/django/core/validators.py#L74
        """
        
        ul = "\u00a1-\uffff"  # Unicode letters range (must not be a raw string).
        # IP patterns
        ipv4_re = (
            r"(?:0|25[0-5]|2[0-4][0-9]|1[0-9]?[0-9]?|[1-9][0-9]?)"
            r"(?:\.(?:0|25[0-5]|2[0-4][0-9]|1[0-9]?[0-9]?|[1-9][0-9]?)){3}"
        )
        ipv6_re = r"\[[0-9a-f:.]+\]"  # (simple regex, validated later)
        # Host patterns
        hostname_re = (
            r"[a-z" + ul + r"0-9](?:[a-z" + ul + r"0-9-]{0,61}[a-z" + ul + r"0-9])?"
        )
        # Max length for domain name labels is 63 characters per RFC 1034 sec. 3.1
        domain_re = r"(?:\.(?!-)[a-z" + ul + r"0-9-]{1,63}(?<!-))*"
        tld_re = (
            r"\."  # dot
            r"(?!-)"  # can't start with a dash
            r"(?:[a-z" + ul + "-]{2,63}"  # domain label
            r"|xn--[a-z0-9]{1,59})"  # or punycode label
            r"(?<!-)"  # can't end with a dash
            r"\.?"  # may have a trailing dot
        )
        host_re = "(" + hostname_re + domain_re + tld_re + "|localhost)"
        regex = re.compile(
            r"^(?:http|ftp)s?://" # http(s):// or ftp(s)://
            r"(?:[^\s:@/]+(?::[^\s:@/]*)?@)?"  # user:pass authentication
            r"(?:" + ipv4_re + "|" + ipv6_re + "|" + host_re + ")"
            r"(?::[0-9]{1,5})?"  # port
            r"(?:[/?#][^\s]*)?"  # resource path
            r"\Z",
            re.IGNORECASE,
        )
        result = re.match(regex, value) is not None
        return result
 
 
    def IP(value) -> bool:
        """ Base IP validator
        
        This will validate both ipv4 and ipv6 using regex library.
        """
        
        flag_string = 'gm' 
        ipv4 = r"(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])"
        #ipv4 = r"^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$"
        ipv6 = r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"
        
        regipv4 = re.compile(ipv4, sum(getattr(re, flag.upper()) for flag in flag_string if flag in "imsluxa"))
        regipv6 = re.compile(ipv6, sum(getattr(re, flag.upper()) for flag in flag_string if flag in "imsluxa"))
        
        boolipv4 = bool(regipv4.match(value))
        boolipv6 = bool(regipv6.match(value))
        
        for boolean in [boolipv4,boolipv6]:
            if boolean == True:
                return True

        return False
    
    
    def validate_file_(value) -> bool:
        """ Validates a value if the value is a path for an existing file """
        
        try:
            file = open(value,'r')
            file.close()
            return True
        except Exception as error:
            print (f"error :: {error}")
            return False
        
        
    def validate_scheme_(value) -> bool:
        """ Validates a value whether if its a scheme or not """
        
        try:
            assert value.lower() in ['http','https']; return True
        except:
            return False
        
        
    def validate_shell_type_(value) -> bool:
        """ Validates a value if its a valid shell type or not """
        
        try:
            assert value.lower() in ['reverse','backdoor']; return True
        except:
            return False


    def validate_cryptographic_hash_(value) -> bool:
        try:
            assert value.lower in ['sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512', 'md5', 'argon2', 'bcrypt']; return True
        except:
            return False        

        
    def validate_wordlist_(value) -> bool:
        """ Validates the value by checking the file extension and file existence """
        
        val = value.split('.')
        try:
            assert val[-1] in ['txt','text']
            try:
                file = open(value)
                file.close()
                return True
            except Exception as error:
                print (f"error :: {error}")
                return False
        except:
            print ('error :: file extension must be .txt or .text')
            return False

    def validate_yaml_(value) -> bool:
        """ Validates the value by checking the file extension and file existence """
        
        val = value.split('.')
        try:
            assert val[-1] in ['yaml','yml']
            try:
                file = open(value)
                file.close()
                return True
            except Exception as error:
                print (f"error :: {error}")
                return False
        except:
            print ('error :: file extension must be .yml or .yaml')
            return False


    def validate_json_(value) -> bool:
        """ Validates the value by checking the file extension and file existence """
        
        val = value.split('.')
        try:
            assert val[-1] == 'json'
            try:
                file = open(value)
                file.close()
                return True
            except Exception as error:
                print (f"error :: {error}")
                return False
        except:
            print ('error :: file extension must be .json')
            return False
    
    
    def validate_timeout_(value) -> bool:
        """ Validates a value by checking if the type of the object is correct """
        
        try:
            # Formatting it to int because the command prompt
            # does not automatically format numbers into int
            # to avoid type errors from libraries.
            if isinstance(int(value), int) == True:
                if 1 <= int(value) <= 100:
                    return True
                else:
                    return False
        except:
            try:
                # Formatting to float even though the command
                # line automatically formats float into float.
                # This is to make sure that before the object
                # entered the opt container, it is in the 
                # correct object type.
                if isinstance(float(value), float) == True:
                    if 0.5 <= float(value) <= 100.00:
                        return True
                    else:
                        return False
            except:
                return False
            
            
    def validate_url_(value) -> bool:
        """ Validates url via using base url validator """
        
        validity = validator.URL(value)
        if validity == False:
            print ('url example -> http://hostname')
            return False
        if validity == True:
            return True


    def validate_iso_(value) -> bool:
        """ Validates if a value is a valid iso-3166 alpha-2 code """
        
        try:
            assert value.upper() in ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR","AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE","BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO","BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD","CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI","HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG","SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF","PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD","GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN","HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT","JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG","LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK","MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT","MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA","NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP","NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN","PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN","LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC","SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES","LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ","TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV","UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN","VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]; return True
        except:
            return False
        
        
    def validate_phone_number_(value) -> bool:
        """ Validates a phone number via checking the type of an object and the length of it """
        
        pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        match = re.search(pattern, value)
        if match:
            return True
        return False
        
        
    def validate_condition_(value) -> bool:
        """ Validates the value by checking whether the value is a boolean or not """
        try:
            assert value.lower() in ['true','false']; return True
        except:
            return False
        
        
    def validate_port_(value) -> bool:
        """ Validates a value by checking the object type and if its inside the range 1-65535 """
        
        port = str(value).isdigit()
        if port == True:
            if 1 <= int(value) <= 65535:
                return True
            else:
                return False
        if port == False:
            return False
        
        
    def validate_port_range_(value) -> bool:
        """ Validates the value by checking if its in the correct format and is in range 1-65535 """
        
        error = []
        if '-' not in value:
            print ('port range format => 80-443')
            return False
        try:
            r1, r2 = value.split('-')
        except Exception as error:
            print (f'error :: {error}')
            print ('port range example => 80-443')
            return False
        range1 = r1.strip(' ')
        if 1 <= int(range1) <= 65535:
            pass
        else:
            error.append(1)
        range2 = r2.strip(' ')
        if 1 <= int(range2) <= 65535:
            pass
        else:
            error.append(1)
            
        if len(error) == 0:
            return True
        if len(error) != 0:
            return False        
        
        
    def validate_socket_type_(value) -> bool:
        """ Validates the value by checking if the value is a valid socket type """
        
        try:
            assert value.upper() in ['SOCK_STREAM', 'SOCK_DGRAM', 'SOCK_RAW', 'SOCK_RDM', 'SOCK_SEQPACKET', 'SOCK_NONBLOCK', 'SOCK_CLOEXEC']; return True
        except:
            return False


    def validate_address_family_(value) -> bool:
        """ Validates the value by checking if the value is a address family """
        
        try:
            assert value.upper() in ['AF_UNSPEC', 'AF_UNIX', 'AF_INET', 'AF_AX25', 'AF_IPX', 'AF_APPLETALK', 'AF_NETROM', 'AF_BRIDGE', 'AF_ATMPVC', 'AF_X25', 'AF_INET6', 'AF_ROSE', 'AF_NETBEUI', 'AF_SECURITY', 'AF_KEY', 'AF_NETLINK', 'AF_ROUTE', 'AF_PACKET', 'AF_ASH', 'AF_ECONET', 'AF_ATMSVC', 'AF_RDS', 'AF_SNA', 'AF_IRDA', 'AF_PPPOX', 'AF_WANPIPE', 'AF_LLC', 'AF_CAN', 'AF_TIPC', 'AF_BLUETOOTH', 'AF_ALG', 'AF_VSOCK', 'AF_QIPCRTR']; return True
        except:
            return False


    def validate_host_(value) -> bool:
        """ Validates a value by checking if its a valid host via base validators """
        
        ip = validator.IP(value)
        if ip == True:
            return True
        url = validator.URL(value)
        if url == True:
            return True
        if url == False:
            print ('url example -> https://hostname')
            
        return False
        
        
    def validate_ip_(value) -> bool:
        """ Validates a value if its an ipv4 or ipv6 via base ip validator """
        
        validity = validator.IP(value)
        if validity == True:
            return True
        if validity == False:
            return False
        
        
    def validate_int_(value) -> bool:
        """ Validates the value by checking if the object type is int """
        
        try:
            if isinstance(int(value),int):
                return True
            return False
        except:
            return False
        

    def validate_float_(value) -> bool:
        """ Validates the value by checking if the object type is float """
        
        try:
            if isinstance(float(value),float):
                return True
            return False
        except:
            return False
        
        
    def validate_protocol_(value) -> bool:
        """ Validates the value by checking if its a valid protocol """
        
        try:
            assert value in ['tcp','udp']; return True
        except:
            return False
        
        
    def validate_http_type_(value) -> bool:
        """ Validates the value by checking if the value is a valid http type """
        
        try:
            assert value in ['HTTP/0.9', "HTTP/1.0", 'HTTP/1.1']; return True
        except:
            return False
        
        
    def validate_http_method_(value) -> bool:
        """ Validates the value by checking whether if the value is a valid http request method """
        
        try:
            assert value.lower() in ['head','get','post','put','patch','delete']; return True
        except:
            return False
        
        
    def validate_bool_(value) -> bool:
        """ Validates the value by checking if the value is a boolean value """
        
        try:
            assert value.lower() in ['true','false']; return True
        except:
            return False
        
    
    def validate_php_function_(value) -> bool:
        """ Validates the value by checking if the value is a valid php function """
        
        try:
            assert value.lower() in ['exec','shell_exec','passthru','system','popen']; return True
        except:
            return False
        