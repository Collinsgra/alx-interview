#!/usr/bin/python3
"""
method that determines if a given data set represents a
valid UTF-8 encoding
"""
def validUTF8(data):
    def is_valid_byte(byte):
        return 0 <= byte <= 255
    
    n_bytes = 0

    for byte in data:
        if not is_valid_byte(byte):
            return False
        
        bin_rep = format(byte, '#010b')[-8:]

        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                n_bytes = 1
            elif bin_rep[:4] == '1110':
                n_bytes = 2
            elif bin_rep[:5] == '11110':
                n_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
            n_bytes -= 1
    
    return n_bytes == 0
