#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
grep_word = sys.argv[1]

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line.find(grepWord) != -1:
        print '%s\t%s' % ( line.strip(),1)    
