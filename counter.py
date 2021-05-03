#!/usr/bin/env python3

"""
@author Isaac Keleher 2021
This is a program to output insights for a flat log file
containing traffic counts

Program Outputs:
    total: total num of cars seen
    daily: yyyy-mm-dd and num cars seen on that day for all cars in input file
    most_cars: top 3 half hours with most cars in same format as input file
    least_cars: the 1.5 hour period with least cars, i.e. three contiguous
    half hour records
"""

import sys
import dateutil.parser
import pandas as pd


def read_file(fname) -> str:
    """You can probably guess what this does by the name.

    Args:
        fname (str): a filename
    Returns:
        log_list (list): a list of tuples containing traffic data
    """
    log_list = []
    # open file and split data into tuples
    with open(fname, 'r') as log:
        lines = log.readlines()
        for line in lines:
            line = line.strip()  # for safety
            log_line = ((line[0:19]), (line[20:len(line)]))
            log_list += [log_line]

    return log_list


def count_total_cars(log_list) -> int:
    """Return the total count of all cars recorded in the log file

    Args:
        log_list (list): a list of tuples
    Returns:
        total (int): sum of all cars counted
    """
    total = 0
    # iterate and sum counts
    for tpl in log_list:
        num = int(tpl[1])
        total += num

    return total


def count_daily_cars(log_list) -> dict:
    """Return the total count of all cars recorded in the log file

    Args:
        log_list (list): a list of tuples
    Returns:
        daily_count_dict (dict): hashmap of car count entries per day
    """
    # use a hashmap to avoid duplicates
    daily_count_dict = {}
    # parse dates and counts
    for tpl in log_list:
        count = int(tpl[1])
        timestamp = tpl[0]
        timestamp = dateutil.parser.isoparse(timestamp)
        date = timestamp.strftime('%Y-%m-%d')
        # use date as the key to find daily count, update as needed
        if date in daily_count_dict.keys():
            count = daily_count_dict[date] + count
            daily_count_dict[date] = count
        else:
            daily_count_dict[date] = count

    return daily_count_dict


def count_most_cars(log_list) -> list:
    """Return the top 3 half hours with the most cars counted

    Args:
        log_list (list): a list of tuples
    Returns:
        top_3_list (list): the top 3 periods
    """
    # sorts in place by count
    log_list.sort(key=lambda tpl: int(tpl[1]), reverse=True)
    # grab top 3
    log_list = log_list[:3]

    top_3_list = []
    # convert tuples to strings and store for return
    for tpl in log_list:
        tpl_str = f'{tpl[0]} {tpl[1]}'
        top_3_list += [tpl_str]

    return top_3_list


def count_least_cars(log_list) -> pd.DataFrame:
    """Returns the 1.5 hour contiguous period with the least cars.

    The email says "assume clean input" but there are many missing
    half hour periods. Rather than just returning "0" I chose to
    drop all numbers and choose the smallest contiguous period that
    is not zero.

    Args:
        log_list: a list of tuples
    Returns:
        min: a string of the format 'yyyy-mm-dd hh-mm-ss'
        followed by a count value
    """
    # sorts in place by timestamp
    log_list.sort(key=lambda tpl: dateutil.parser.isoparse(tpl[0]))

    # create a dataframe with appropriate types for our operations
    df = pd.DataFrame(log_list, columns=['time', 'count'])
    df['time'] = pd.to_datetime(df['time'])
    df['count'] = pd.to_numeric(df['count'], downcast='integer')

    # resample the dataframe to get 1.5 hour contigous periods over a day
    df_resampled = df.resample(
        '1.5H', on='time', origin='start', closed='left'
    ).sum()

    # grab row by min count and return string
    # comment below line for 1/2 hr periods of count 0
    df_resampled = df_resampled[(df_resampled != 0).all(1)]
    min = df_resampled[df_resampled['count'] == df_resampled['count'].min()]
    min = f'{min.index[0]} {min.values[0][0]}'

    return min


if __name__ == "__main__":

    if len(sys.argv) > 1:
        fname = sys.argv[1]  # take input file
    else:
        fname = 'traffic.log'

    log = read_file(fname)

    total = count_total_cars(log)
    daily = count_daily_cars(log)
    most_cars = count_most_cars(log)
    least_cars = count_least_cars(log)

    print('============= Total ============')
    print(total)
    print('============= Daily ============')
    for line in daily:
        print(f'{line} {daily[line]}')
    print('============= Most =============')
    for line in most_cars:
        print(line)
    print('============= Least ============')
    print(least_cars)
