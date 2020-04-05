#!/usr/bin/env python
"""mapper.py"""

import sys
import re
pattern = sys.argv[1]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    ip = words[0]
    print '%s\t%s' % (ip, 1)
