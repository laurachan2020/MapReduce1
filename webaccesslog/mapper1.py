#!/usr/bin/env python
"""mapper1.py"""

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
            print '%s\t%s' % (words[0], 1)
