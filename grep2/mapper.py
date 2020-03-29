#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
if len(argv) >= 2:
    grep_word = argv[1]

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line.find(grepWord) != -1:
        print '%s\t%s' % ( grepWord, line.strip() )    
