#!/usr/bin/env python
"""mapper2.py"""
import sys
import re
import time
pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
datetime_pattern = '%d/%b/%Y:%H:%M:%S'

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    if len(words)==4:
        test = pat.match(words[0])
        if test:
            try:
                log_time = time.strptime(words[1][1:],datetime_pattern)
                if log_time.tm_hour < 12:
                    print '%s\t%s' % ('beforenoon', 1)
                else:
                    print '%s\t%s' % ('afternoon', 1)
            except Exception:
                pass

