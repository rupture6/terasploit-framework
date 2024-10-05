#######
# Formatter: Fix Data Type
#######

from __future__ import annotations

class DataType:
    
    @staticmethod
    def float_and_any(value) -> float|any:
        try:
            return float(value)
        except:
            return value
        
    
    @staticmethod
    def int_float_any(value) -> int|float|any:
        try:
            return float(value)
        except:
            try:
                return int(value)
            except:
                return value