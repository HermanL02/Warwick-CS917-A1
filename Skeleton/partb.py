import csv
# import time module to handle time conversions
import time
# import calendar module to handle calendar conversions
import calendar
# import sys (which is mentioned in the FAQ)
import  sys
"""
    Part B
    Please provide definitions for the following functions *WITH EXCEPTION HANDLERS*
"""

"""
Please note: I do not use this file to do the testing, I used the unit tests which is a more efficient way and 
more likely to be the industry standard. Therefore, the main part only contains the import file part, but not the 
actual testing of the functions. """


# define a Exception_Handler class
class Exception_Handler(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return self.parameter


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# end_date: string in "dd/mm/yyyy" format

def highest_price(data, start_date, end_date):
    # exception handling of the start date and end date
    try:
        # start_timestamp: the timestamp of the start date
        start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        # end_timestamp: the timestamp of the end date
        end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError as e:
        print("Error: invalid date value")
        sys.exit()
    try:
        if end_timestamp < start_timestamp:
            raise Exception_Handler("Error: end date is before start date")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # exception handling of the out of range date
    try:
        if end_timestamp > int(data[-1]['time']):
            raise Exception_Handler("Error: date value is out of range")
        if start_timestamp < int(data[0]['time']):
            raise Exception_Handler("Error: date value is out of range")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # highest: the return value, which means highest_price
    highest = 0.0
    # exception handling of the missing column
    try:
        for i in data:
            if int(i['time']) < start_timestamp:
                continue
            if int(i['time']) > end_timestamp:
                break
            if float(i['high']) > highest:
                # if the high price is higher than the highest price, update the highest price
                highest = float(i['high'])
    except KeyError as e:
        print("Error: requested column is missing from dataset")
        sys.exit()
    return highest


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    # exception handling of the start date and end date
    try:
        # replace None with an appropriate return value
        # start_timestamp: the timestamp of the start date
        start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        # end_timestamp: the timestamp of the end date
        end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError as e:
        print("Error: invalid date value")
        sys.exit()
    try:
        if end_timestamp < start_timestamp:
            raise Exception_Handler("Error: end date is before start date")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # exception handling of the out of range date
    try:
        if end_timestamp > int(data[-1]['time']):
            raise Exception_Handler("Error: date value is out of range")
        if start_timestamp < int(data[0]['time']):
            raise Exception_Handler("Error: date value is out of range")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # lowest: the return value, which means lowest_price
    lowest = 0.0
    # flag: help to define the lowest as the first value within the time range
    flag = True
    # for loop to find the lowest price
    # exception handling of the missing column
    try:
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
    except KeyError as e:
        print("Error: requested column is missing from dataset")
        sys.exit()

    return lowest


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    # exception handling of the start date and end date
    try:
        # replace None with an appropriate return value
        # start_timestamp: the timestamp of the start date
        start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        # end_timestamp: the timestamp of the end date
        end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError as e:
        print("Error: invalid date value")
        sys.exit()
    # exception handling of the out of range date
    try:
        if end_timestamp < start_timestamp:
            raise Exception_Handler("Error: end date is before start date")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    try:
        if end_timestamp > int(data[-1]['time']):
            raise Exception_Handler("Error: date value is out of range")
        if start_timestamp < int(data[0]['time']):
            raise Exception_Handler("Error: date value is out of range")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # max_volume: the return value, which means max_volume
    max_vol = 0.0
    # for loop to find the lowest price
    # Exception handling of the missing column
    try:
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
    except KeyError as e:
        print("Error: requested column is missing from dataset")
        sys.exit()
    return max_vol


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    # exception handling of the start date and end date
    try:
        # replace None with an appropriate return value
        # start_timestamp: the timestamp of the start date
        start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        # end_timestamp: the timestamp of the end date
        end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError as e:
        print("Error: invalid date value")
        sys.exit()
    try:
        if end_timestamp < start_timestamp:
            raise Exception_Handler("Error: end date is before start date")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    try:
        if end_timestamp > int(data[-1]['time']):
            raise Exception_Handler("Error: date value is out of range")
        if start_timestamp < int(data[0]['time']):
            raise Exception_Handler("Error: date value is out of range")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # best_avg_price: the return value, which means best_avg_price
    best_price = 0.0
    # for loop to find the best price
    # exception handling of the missing column
    try:
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
    except KeyError as e:
        print("Error: requested column is missing from dataset")
        sys.exit()
    return best_price


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    # exception handling of the start date and end date
    try:
        # replace None with an appropriate return value
        # start_timestamp: the timestamp of the start date
        start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        # end_timestamp: the timestamp of the end date
        end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError as e:
        print("Error: invalid date value")
        sys.exit()
    # exception handling of the out of range date
    try:
        if end_timestamp < start_timestamp:
            raise Exception_Handler("Error: end date is before start date")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # exception handling of the out of range date
    try:
        if end_timestamp > int(data[-1]['time']):
            raise Exception_Handler("Error: date value is out of range")
        if start_timestamp < int(data[0]['time']):
            raise Exception_Handler("Error: date value is out of range")
    except Exception_Handler as e:
        print(e)
        sys.exit()
    # best_avg_price: the return value, which means best_avg_price
    avg = 0.0
    # avg list
    avg_list = []
    # for loop to find the best price
    # Exception handling of the missing column
    try:
        for i in data:
            # if the time is before the start date, continue
            if int(i['time']) < start_timestamp:
                continue
            # if the time is after the end date, break
            if int(i['time']) > end_timestamp:
                break
            # find the best price
            avg_list.append(float(i['volumeto']) / float(i['volumefrom']))
    except KeyError as e:
        print("Error: requested column is missing from dataset")
        sys.exit()
    # calculate the average and to two decimal places
    avg = round(sum(avg_list) / len(avg_list), 2)
    return avg


# Please note:
if __name__ == "__main__":
    # Start the program
    # data is always the cryptocompare_btc.csv read in using a DictReader
    data = []
    # Exception handling of the missing file
    try:
        with open("../cryptocompare_btc.csv", "r") as f:
            reader = csv.DictReader(f)
            data = [r for r in reader]
    except FileNotFoundError:
        print("Error: dataset not found")
        sys.exit()
    highest_price(data, "01/012000", "31/01/2016")
    pass
