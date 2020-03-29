#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
first = True
for line in sys.stdin:
    if first:
        first = false;
        grepWord = line.strip()
        continue

    if line.find(grepWord) != -1:
        print '%s\t%s' % ( grepWord, line.strip() )
