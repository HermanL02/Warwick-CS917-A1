# Import csv module to handle csv files
import csv
# Import time module to handle time conversions
import time
# Import calendar module to handle calendar conversions
import calendar

"""Part A 
# Note: 1/ I have confirmed with TA, that if the cryptocompare_btc.csv has a from small to large time 
order, then the testing done by professor would use the same order. """


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
    lowest = 0.0
    # For Initial a lowest price value
    flag = True
    # for loop to find the lowest price
    for i in data:
        # if the time is before the start date, continue
        if int(i['time']) < start_timestamp:
            continue
        # if the time is after the end date, break
        if int(i['time']) > end_timestamp:
            break
        # if the time is between the start date and the end date, set the flag to True
        if start_timestamp <= int(i['time']) <= end_timestamp and flag:
            lowest = float(i['low'])
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
    max_vol = 0.0
    # for loop to find the lowest price
    for i in data:
        # if the time is before the start date, continue
        if int(i['time']) < start_timestamp:
            continue
        # if the time is after the end date, break
        if int(i['time']) > end_timestamp:
            break
        # if the volume is higher than the max volume, update the max volume
        if max_vol < float(i['volumefrom']):
            max_vol = float(i['volumefrom'])
    return max_vol


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    # replace None with an appropriate return value
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # best_avg_price: the return value, which means best_avg_price
    best_price = 0.0
    # for loop to find the best price
    for i in data:
        # if the time is before the start date, continue
        if int(i['time']) < start_timestamp:
            continue
        # if the time is after the end date, break
        if int(i['time']) > end_timestamp:
            break
        # find the best price
        if float(i['volumeto']) / float(i['volumefrom']) > best_price:
            best_price = float(i['volumeto']) / float(i['volumefrom'])
    return best_price


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    # replace None with an appropriate return value
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    avg = 0.0
    # avg list
    avg_list = []
    # for loop to find the best price
    for i in data:
        # if the time is before the start date, continue
        if int(i['time']) < start_timestamp:
            continue
        # if the time is after the end date, break
        if int(i['time']) > end_timestamp:
            break
        # find the best price
        avg_list.append(float(i['volumeto']) / float(i['volumefrom']))
    # calculate the average and to two decimal places
    avg = round(sum(avg_list) / len(avg_list), 2)
    return avg
