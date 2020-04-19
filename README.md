# string extractor
extracts all plausible strings from a given file

# Usage

strings.py |-n min_length| |-e encoding| |filename|

min_length: All plausible strings less than the min_length will not be included in the output

encoding: Select the character encoding of the strings that are to be found. 
          Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, l = little endian UTF-16.
              
filename: the name of the file to extract from


