# Import csv module to handle csv files
import csv
# Import time module to handle time conversions
import time
# Import calendar module to handle calendar conversions
import calendar

"""
    Part C
    Please provide definitions for the following functions
"""


# moving_avg_short(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_short(data, start_date, end_date):
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # avg_dict: the return value, which means moving_avg_short
    avg_dict = {}
    # for loop to find the moving average
    for i in range(len(data)):
        if int(data[i]['time']) < start_timestamp:
            continue
        if int(data[i]['time']) > end_timestamp:
            break
        # Define avg_list, total and avg
        avg_list = []
        total = 0.0
        avg = 0.0
        # If "i" is the first 2 days of CSV
        if i < 2:
            for j in range(i + 1):
                total += float(data[i]['volumeto']) / float(data[i]['volumefrom'])
            avg = total / (i + 1)
        else:
            total = float(data[i]['volumeto']) / float(data[i]['volumefrom']) + float(data[i - 1]['volumeto']) / float(
                data[i - 1]['volumefrom']) + float(data[i - 2]['volumeto']) / float(data[i - 2]['volumefrom'])
            avg = total / 3
        avg_dict[int(data[i]['time'])] = float(avg)
    return avg_dict


# moving_avg_long(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_long(data, start_date, end_date):
    # start_timestamp: the timestamp of the start date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    # end_timestamp: the timestamp of the end date
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # avg_dict: the return value, which means moving_avg_short
    avg_dict = {}
    # for loop to find the moving average
    for i in range(len(data)):
        if int(data[i]['time']) < start_timestamp:
            continue
        if int(data[i]['time']) > end_timestamp:
            break
        # Define avg_list, total and avg
        avg_list = []
        total = 0.0
        avg = 0.0
        # If "i" is the first 10 days of CSV
        if i < 9:
            for j in range(i + 1):
                total += float(data[i]['volumeto']) / float(data[i]['volumefrom'])
            avg = total / (i + 1)
        else:
            for j in range(i - 9, i + 1):
                total += float(data[j]['volumeto']) / float(data[j]['volumefrom'])
            avg = total / 10
        avg_dict[int(data[i]['time'])] = float(avg)
    return avg_dict


# find_buy_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_buy_list(short_avg_dict, long_avg_dict):
    # buy_dict: the return value, which means buy_list when value is 1
    buy_dict = {}
    # sorted_keys: the sorted keys of short_avg_dict
    sorted_keys = sorted(short_avg_dict.keys())
    # for loop to find the buy list
    for i in range(1, len(sorted_keys)):
        current_key = sorted_keys[i]
        prev_key = sorted_keys[i - 1]
        # The logic is based on the document
        if short_avg_dict[prev_key] < long_avg_dict[prev_key] and short_avg_dict[current_key] > long_avg_dict[
            current_key]:
            # Convert the timestamp to date
            dt = time.gmtime(current_key)
            time_string = time.strftime("%d/%m/%Y", dt)
            buy_dict[time_string] = 1
    return buy_dict


# find_sell_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_sell_list(short_avg_dict, long_avg_dict):
    # sell_dict: the return value, which means sell_list when value is 1
    sell_dict = {}
    # sorted_keys: the sorted keys of short_avg_dict
    sorted_keys = sorted(short_avg_dict.keys())
    # for loop to find the sell list
    for i in range(1, len(sorted_keys)):
        current_key = sorted_keys[i]
        prev_key = sorted_keys[i - 1]
        # The logic is based on the document
        if short_avg_dict[prev_key] > long_avg_dict[prev_key] and short_avg_dict[current_key] < long_avg_dict[
            current_key]:
            # Convert the timestamp to date
            dt = time.gmtime(current_key)
            time_string = time.strftime("%d/%m/%Y", dt)
            sell_dict[time_string] = 1
    return sell_dict


# crossover_method(data, start_date, end_date) -> [buy_list, sell_list]
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def crossover_method(data, start_date, end_date):
    long_avg_dict = moving_avg_long(data, start_date, end_date)
    short_avg_dict = moving_avg_short(data, start_date, end_date)
    # buy list where find_buy_list dictionary value is 1
    # A list induction is used to find the buy list and sell list easily instead of using the for loop shown below
    # result_dict = find_buy_list(short_avg_dict, long_avg_dict)
    # buy_list = []
    # for key, value in result_dict.items():
    # if value == 1:
    # buy_list.append(key)
    buy_list = buy_list = [key for key, value in find_buy_list(short_avg_dict, long_avg_dict).items() if value == 1]
    # sell list where find_sell_list dictionary value is 1
    sell_list = sell_list = [key for key, value in find_sell_list(short_avg_dict, long_avg_dict).items() if value == 1]
    return [list(buy_list), list(sell_list)]


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader
    data = []
    with open("../cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    print(crossover_method(data, "01/05/2017", "12/06/2017"))
