import argparse
import struct

def utf8(file, min_len, size):
    scan = 0
    string = ''
    
    for i in range(size):
        while bytes([0x20]) <= file[scan:scan + 1] <= bytes([0x7E]):
            string += bytes.decode(file[scan:scan + 1])
            scan += 1
        if len(string) >= min_len:
            print(string)
        string = ''
        scan += 1
    return

def utf16_be(file, min_len, size):
    scan = 1
    string = ''
    
    while scan < size:
        byte = struct.unpack('BB', file[scan - 1:scan + 1])
        while (0x20 <= byte[1] <= 0x7E) & (byte[0] == 0):
            string += chr(byte[1])
            if scan + 2 >= size:
                break
            else:
                scan += 2
                byte = struct.unpack('BB', file[scan - 1:scan + 1])
        if len(string) >= min_len:
            print(string)
        string = ''
        scan += 2
    return

def utf16_le(file, min_len, size):
    scan = 0
    string = ''
    
    while scan < size - 2:
        byte = struct.unpack('BB', file[scan:scan + 2])
        while (0x20 <= byte[0] <= 0x7E) & (byte[1] == 0):
            string += chr(byte[0])
            if scan + 2 >= size:
                break
            else:
                scan += 2
                byte = struct.unpack('BB', file[scan:scan + 2])
        if len(string) >= min_len:
            print(string)
        string = ''
        scan += 2
    return

def print_strings(file_obj, encoding, min_len):
    
    data = file_obj.read()
    size = len(data)
    
    if encoding == 's':  # UTF-8 printable ASCII
        utf8(data, min_len, size)
    elif encoding == 'b':   # Big endian UTF-16
        utf16_be(data, min_len, size)
    else:
        utf16_le(data, min_len, size)

def main():
    parser = argparse.ArgumentParser(description='Print the printable strings from a file.')
    parser.add_argument('filename')
    parser.add_argument('-n', metavar='min-len', type=int, default=4,
                        help='Print sequences of characters that are at least min-len characters long')
    parser.add_argument('-e', metavar='encoding', choices=('s', 'l', 'b'), default='s',
                        help='Select the character encoding of the strings that are to be found. ' +
                             'Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, ' +
                             'l = little endian UTF-16.')
    args = parser.parse_args()

    with open(args.filename, 'rb') as f:
        print_strings(f, args.e, args.n)

if __name__ == '__main__':
    main()