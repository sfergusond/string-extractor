
def encode(codepoint):
    if codepoint < 128:
        return bytes([codepoint])
    elif 128 <= codepoint <= 0x7FF:
        # Low-order byte
        template = 0b10000000; mask = 0b111111 
        byte0 = codepoint & mask
        b0 = template | byte0
        
        # High-order byte
        template = 0b11000000; shifted = codepoint >> 6
        b1 = template | shifted
        
        return bytes([b1, b0])
    elif 0x800 <= codepoint <= 0xFFFF:
        # Lowest-order byte
        template = 0b10000000; mask = 0b111111
        byte0 = codepoint & mask
        b0 = template | byte0
        
        # Low-order byte
        template = 0b10000000; mask = 0b111111000000
        byte1 = (codepoint & mask) >> 6
        b1 = template | byte1
        
        # High-order byte
        template = 0b11100000; shifted = codepoint >> 12
        b2 = template | shifted
        
        return bytes([b2, b1, b0])
    else:
        # Lowest-order byte
        template = 0b10000000; mask = 0b111111
        byte0 = codepoint & mask
        b0 = template | byte0
        
        # Second Lowest-order byte
        template = 0b10000000; mask = 0b111111000000
        byte1 = (codepoint & mask) >> 6
        b1 = template | byte1
        
        # Low-order byte
        template = 0b10000000; mask = 0b111111000000000000
        byte2 = (codepoint & mask) >> 12
        b2 = template | byte2
        
        # High-order byte
        template = 0b11110000; shifted = codepoint >> 18
        b3 = template | shifted
        
        return bytes([b3, b2, b1, b0])
        
def decode(byte_obj):
    if len(byte_obj) == 1:
        return byte_obj[0]
    elif len(byte_obj) == 2:
        mask = 0b00011111
        b0 = (mask & byte_obj[0]) << 6
        
        mask = 0b00111111
        b1 = mask & byte_obj[1]
        
        return (b0 | b1)
    elif len(byte_obj) == 3:
        mask = 0b00001111
        b0 = (mask & byte_obj[0]) << 12
        
        mask = 0b00111111
        b1 = (mask & byte_obj[1]) << 6
        b2 = mask & byte_obj[2]
        
        return (b0 | b1 | b2)
    else:
        mask = 0b00000111
        b0 = (mask & byte_obj[0]) << 18
        
        mask = 0b00111111
        b1 = (mask & byte_obj[1]) << 12
        b2 = (mask & byte_obj[2]) << 6
        b3 = mask & byte_obj[3]
        
        return (b0 | b1 | b2 | b3)

def main():
    pass

if __name__ == '__main__':
    main()