#!/usr/bin/env python
"""mapper2.py"""
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    if len(words)==4:
        if words[2].startswith('GET')  or words[2].startswith('PUT') or words[2].startswith('POST') or \
                words[2].startswith('DELETE') or words[2].startswith('PATCH'):
            elements = words[2].split()
            if '.php' in elements[1]:
                index = elements[1].index('.php')
                pagename = elements[1].[:index+4]
                print '%s\t%s' % (pagename, 1)
