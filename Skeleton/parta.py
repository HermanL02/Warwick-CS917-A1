# Import csv module to handle csv files
import csv
# Import time module to handle time conversions
import time
# Import calendar module to handle calendar conversions
import calendar

"""
    Part A
    Please provide definitions for the following functions
"""


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# end_date: string in "dd/mm/yyyy" format

def highest_price(data, start_date, end_date):
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # highest: the return value, which means highest_price
    highest = 0.0

    for i in data:
        if int(i['time']) < start_timestamp:
            continue
        if int(i['time']) > end_timestamp:
            break
        if float(i['high']) > highest:
            # if the high price is higher than the highest price, update the highest price
            highest = float(i['high'])
    return highest


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    # replace None with an appropriate return value
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # lowest: the return value, which means lowest_price
    lowest = data[0]['low']
    # for loop to find the lowest price
    for i in data:
        # For Initial a lowest price value
        flag = True
        # if the time is before the start date, continue
        if int(i['time']) < start_timestamp:
            continue
        # if the time is after the end date, break
        if int(i['time']) > end_timestamp:
            break
        # if the time is between the start date and the end date, set the flag to True
        if start_timestamp <= int(i['time']) <= end_timestamp and flag:
            lowest = lowest = float(i['low'])
            flag = False
        # if the low price is lower than the lowest price, update the lowest price
        if float(i['low']) < lowest:
            lowest = float(i['low'])
    return lowest


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    # replace None with an appropriate return value
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # max_volume: the return value, which means max_volume
    max_volume = data[0]['volumefrom']
    # for loop to find the lowest price
    for i in data:
        # if the time is before the start date, continue
        if i['time'] < start_timestamp:
            continue
        # if the time is after the end date, break
        if i['time'] > end_timestamp:
            break
        # if the volume is higher than the max volume, update the max volume
        if i['volumefrom'] > max_volume:
            max_volume = i['volumefrom']
    return max_volume

# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    # replace None with an appropriate return value
    return None


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    # replace None with an appropriate return value
    return None

if __name__ == '__main__':
    print("Testing code is put in tests.py")

