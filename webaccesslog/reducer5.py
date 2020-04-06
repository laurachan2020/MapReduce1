#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_ip_address = None
current_page_name = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    ip_address, page_name, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    pageDic = {}

    if current_ip_address == ip_address:
        if pageDic[page_name]:
            pageDic[page_name] += count
        else:
            pageDic[page_name] = count
    else:
        if current_ip_address and current_page_name and current_count:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_ip_address, current_page_name, current_count)
        current_count = count
        current_ip_address = ip_address
        current_page_name = page_name

# do not forget to output the last word if needed!
if current_ip_address == ip_address and current_page_name and current_count:
    print '%s\t%s\t%s' % (current_ip_address, current_page_name,current_count)
