#!/usr/bin/env python3
import os
import sys
import dateutil.parser
import pandas as pd
import datetime

"""You can probably guess what this does by the name.

Args:
    fname (str): a filename
Returns:
    log: file contents of recorded traffic log
"""
def read_file(fname) -> str:
    # hopefully this path works on windows/linux
    __location__ = os.path.realpath(
    os.path.join(sys.path[0], fname))

    log_list = []

    with open(fname, 'r') as log:
        lines = log.readlines()
        for line in lines:
            line = line.strip() # for safety
            log_line = ((line[0:19]), (line[20:len(line)]))
            log_list += [log_line]

    return log_list

def count_total_cars(log_list) -> int:
    total = 0
    for tpl in log_list:
        num = int(tpl[1])
        total += num
    return total

"""
outputs:
total num of cars seen
yyyy-mm-dd and num cars seen on that day for all cars in input file
top 3 half hours with most cars in same format as input file
the 1.5 hour period with least cars, i.e. 3 contiguous half hour records
"""
if __name__ == "__main__":

    if sys.argv[1]:
        fname = sys.argv[1]
    else:
        fname = 'traffic.log'
    
    log = read_file(fname)

    print(log)
