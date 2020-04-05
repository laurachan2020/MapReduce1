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
    if len(words)==4:
        test = pat.match(words[0])
        if test:
            elements = words[2].split()
            if '.php' in elements[1]:
                index = elements[1].index('.php')
                if elements[1].startswith("//"):
                    pagename = elements[1][2:index+4]
                elif elements[1].startswith("/"):
                    pagename = elements[1][1:index + 4]
                else:
                    pagename = elements[1][0:index + 4]
                print '%s\t%s' % (pagename, 1)

