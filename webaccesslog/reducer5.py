#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_ip_address = None
current_page_name = None
current_count = 0
pageDic = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    combined_key, count = line.split('\t', 1)
    ip_address, page_name = combined_key.split('\:', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer


    if current_ip_address == ip_address:
        if pageDic[ip_address] == None:
            pageDic[ip_address] = {}
            pageDic[ip_address][page_name] = 1
        elif pageDic[ip_address][page_name] == None:
            pageDic[ip_address][page_name] = 1
        else:
            pageDic[ip_address][page_name] += count
        current_count = pageDic[ip_address][page_name]
    else:
        if current_ip_address and current_page_name and current_count:
            # write result to STDOUT
            two_keys=current_ip_address+':'+current_page_name
            print '%s\t%s' % (two_keys, current_count)
        current_count = count
        current_ip_address = ip_address
        current_page_name = page_name

# do not forget to output the last word if needed!
if current_ip_address == ip_address and current_page_name and current_count:
    two_keys = current_ip_address+':'+current_page_name
    print '%s\t%s' % (two_keys, current_count)
