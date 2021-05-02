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

def count_daily_cars(log_list) -> dict:
    # use a hashmap to avoid duplicates
    daily_count_dict = {}

    for tpl in log_list:
        count = int(tpl[1])
        timestamp = tpl[0]
        timestamp = dateutil.parser.isoparse(timestamp)
        date = timestamp.strftime('%Y-%m-%d')

        if date in daily_count_dict.keys():
            count = daily_count_dict[date] + count
            daily_count_dict[date] = count
        else:
            daily_count_dict[date] = count
        # print(dt_object)
        # print(type(dt_object))
    return daily_count_dict


"""Return the top 3 half hours with the most cars counted

It is assumed that these are non-contigous individual half hour periods
"""
def count_most_cars(log_list) -> list:

    log_list.sort(key=lambda tpl: int(tpl[1]), reverse=True)  # sorts in place by count
    log_list = log_list[:3] # grab top 3

    top_3_list = []

    for tpl in log_list:
        # print(tpl)
        tpl_str = f'{tpl[0]} {tpl[1]}'
        # print(type(tpl_str))
        top_3_list += [tpl_str]

    return top_3_list

"""Returns the 1.5 hour contiguous period with the least cars.
"""
def count_least_cars(log_list) -> str:

    # sorts in place by timestamp
    log_list.sort(key=lambda tpl: dateutil.parser.isoparse(tpl[0]))  

    # create a dataframe with appropriate types for our operations
    df = pd.DataFrame(log_list, columns =['time', 'count'])
    df['time']= pd.to_datetime(df['time'])
    df['count']= pd.to_numeric(df['count'], downcast='integer')

    # time_period = datetime.timedelta(hours=1, minutes=30)

    # print(df_resample.dtypes)

    df_resampled = df.resample('1.5H', on='time', origin='start').sum()

    print(df_resampled.to_string())
    # the email says "assume clean input" but there are many missing half hour periods
    # thus we return zero as the min.
    # i've included maximum here for testing purposes

    max = df_resampled[df_resampled['count']==df_resampled['count'].max()]
    min = df_resampled[df_resampled['count']==df_resampled['count'].min()]
    # print(max)
    # print(min)



    # df.resample("90T").sum()
    # df['date'] = pd.to_datetime(df['date'])
    # df = df['cumsum'].resample('90T', on='timestamp').sum()
    # df['newsum'] = df['count'].resample('W', on='timestamp').transform('sum')

    # print(df)

    # # grab the highest num so far
    # log_list.sort(key=lambda tpl: int(tpl[1]), reverse=True)  # sorts in place
    # min = int(log_list[:1][0][1]) 
    # # min = min[0][1]
    # print(f'min {min}')

    # group subdates by day
    # a dictionary of lists containing tuples...
    # day_log_dict = {}

    # for tpl in log_list:
    #     timestamp = tpl[0]
    #     timestamp = dateutil.parser.isoparse(timestamp)
    #     date = timestamp.strftime('%Y-%m-%d')        

    #     if date in day_log_dict.keys():
    #         day_log_dict[date] += [tpl]
    #     else:
    #         tpl_list = [tpl]
    #         day_log_dict[date] = tpl_list

    # analysis 1.5 hour periods

            
    # print
    # print(day_log_dict)


"""
outputs:
total num of cars seen
yyyy-mm-dd and num cars seen on that day for all cars in input file
top 3 half hours with most cars in same format as input file
the 1.5 hour period with least cars, i.e. 3 contiguous half hour records
"""
if __name__ == "__main__":

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = 'traffic.log'
    
    log = read_file(fname)
    # print(log)

    total_count = count_total_cars(log)
    # print(total_count)

    daily_count = count_daily_cars(log)
    # print(daily_count)

    most_cars_count = count_most_cars(log)
    # print(most_cars_count)

    least_cars_count = count_least_cars(log)
    # print(least_cars_count)


