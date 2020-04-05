#!/usr/bin/env python
"""mapper2.py"""
import sys
import re
pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    try:
        if len(words)==4:
            test = pat.match(words[0])
            if test:
                if words[2].startswith('GET')  or words[2].startswith('PUT') or words[2].startswith('POST') or words[2].startswith('DELETE'):
                    elements = words[2].split()
                    if '.php' in elements[1]:
                        index = elements[1].index('.php')
                        pagename = elements[1].[:index+4]
                        print '%s\t%s' % (pagename, 1)
    except:
        pass

