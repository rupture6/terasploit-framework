#######
# Formatter: Fix Data Type
#######

from __future__ import annotations

class DataType:
            
    def float_and_any(value) -> float|any:
        try:
            """ Format string to float. (For options and others)
            
            NOTE: This function prioritize returning float and any objects
            
            Formatting value into to float because it will 
            never be a float if it's in string format. It
            does not check whether the value is float or
            not float.
            
            The goal here is to check if an str object
            can be formatted to float, otherwise it will
            return it as any object.
            """
            if isinstance(float(value), float) == True:
                return float(value)
        except:
            return value
        
    def int_float_any(value) -> int|float|any:
        try:
            """ Object formatter (For clients and others)
            
            NOTE: This function prioritize returning int, float and any objects
            
            This was made to not interfere with other libraries that 
            does not need int objects. This is made for specific 
            functions that requires automatic object formatter.
            """
            
            if isinstance(float(value), float) == True:
                return float(value)
        except:
            try:
                if isinstance(int(value), int) == True:
                    return int(value)
            except:
                return value