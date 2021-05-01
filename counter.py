#!/usr/bin/env python3
import os
import sys

"""You can probably guess what this does by the name.

Args:
    fname (str): a filename
Returns:
    log: file contents of recorded traffic log
"""
def read_file(fname) -> str:
    __location__ = os.path.realpath(
    os.path.join(sys.path[0], fname))
    log = open(fname, 'r')
    return log.read()

def count_total_cars():
    pass

def count_daily_cars():
    pass

def count_most_cars():
    pass

def count_least_cars():
    pass

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
