# string extractor
extracts all plausible strings from a given file

# Usage

strings.py |-n min_length| |-e encoding| |filename|

min_length: All plausible strings less than the min_length will not be included in the output

encoding: Select the character encoding of the strings that are to be found. 
          Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, l = little endian UTF-16.
              
filename: the name of the file to extract from

# Example

strings.py -n 15 test.doc

\# -\*- coding: utf-8 -\*-
Created on Sun Feb 10 17:54:59 2019
\[Content_Types].xml
theme/theme/themeManager.xml
theme/theme/theme1.xml
theme/theme/\_rels/themeManager.xml.rels
\[Content_Types].xmlPK
theme/theme/themeManager.xmlPK
theme/theme/theme1.xmlPK
theme/theme/\_rels/themeManager.xml.relsPK
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:clrMap xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
Spencer Ferguson-Dryden
Spencer Ferguson-Dryden
Microsoft Office Word
Microsoft Word 97-2003 Document
Word.Document.8


