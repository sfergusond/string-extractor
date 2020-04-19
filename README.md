# string extractor
extracts all plausible strings from a given file

# Usage

strings.py |-n min_length| |-e encoding| |filename|

min_length: All plausible strings less than the min_length will not be included in the output

encoding: Select the character encoding of the strings that are to be found. 
          Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, l = little endian UTF-16.
              
filename: the name of the file to extract from

# Example

strings.py test.doc

bjbj
\# -\*- coding: utf-8 -\*-
Created on Sun Feb 10 17:54:59 2019
@author: sferg
hello world!
gdPl
\[Content_Types].xml
_rels/.rels
theme/theme/themeManager.xml
sQ}#
theme/theme/theme1.xml
w toc'v
)I\`n
3Vq%'#q
:\TZaG
L+M2
e\O*
$*c?
Qg20pp
\}DU4
hsF+
,)''K
K4'+
vt]K
O@%\w
S; Z
|s*Y
0X4D)
?*|f
-45x
/Y|t
theme/theme/_rels/themeManager.xml.rels
6?$Q
K(M&$R(.1
\[Content_Types].xmlPK
_rels/.relsPK
theme/theme/themeManager.xmlPK
theme/theme/theme1.xmlPK
theme/theme/_rels/themeManager.xml.relsPK
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:clrMap xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
\[r'S\r'
Spencer Ferguson-Dryden
Normal.dotm
Spencer Ferguson-Dryden
Microsoft Office Word
Title
Microsoft Word 97-2003 Document
MSWordDoc
Word.Document.8


