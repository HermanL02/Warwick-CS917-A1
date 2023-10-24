import matplotlib.pyplot as plt
import csv
import calendar
import sys
import time

"""
    Part D
    Please provide definitions for the following class and functions
"""
"""
    References: (For helping me to better understand the linear regression) 
    1. https://www.w3schools.com/python/python_ml_linear_regression.asp  This website gives me a clear view of
    how they use the linear regression module in Python. 
    2. https://www.linkedin.com/pulse/how-write-your-own-linear-regression-algorithm-python-daniel-afriyie/ This 
    website introduces one way that can build a linear regression in Python. 
"""


# Define a Exception_Handler class
class Exception_Handler(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return self.parameter


"""
# Class Investment:
# Instance variables
#	start date
#	end date
#	data 
# Functions
#	highest_price(data, start_date, end_date) -> float
#	lowest_price(data, start_date, end_date) -> float
#	max_volume(data, start_date, end_date) -> float
#	best_avg_price(data, start_date, end_date) -> float
#	moving_average(data, start_date, end_date) -> float
"""


class Investment:
    def __init__(self, start_date: str, end_date: str, data: dict):
        self.start_date = start_date
        self.end_date = end_date
        self.data = data

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
        # Exception handling of the start date and end date
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
        # lowest: the return value, which means lowest_price
        lowest = 0.0
        # for Initial a lowest price value
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
        # exception handling of the missing column
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
        # Exception handling of the start date and end date
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
        # Exception handling of the start date and end date
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
        avg = 0.0
        # avg list
        avg_list = []
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
                avg_list.append(float(i['volumeto']) / float(i['volumefrom']))
        except KeyError as e:
            print("Error: requested column is missing from dataset")
            sys.exit()
        # calculate the average and to two decimal places
        avg = round(sum(avg_list) / len(avg_list), 2)
        return avg


# predict_next_average(investment) -> float
# investment: Investment type
def predict_next_average(investment):
    data, start_date, end_date = investment.data, investment.start_date, investment.end_date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # x: the list of time
    x = []
    # y: the list of average price
    y = []
    for i in data:
        if start_timestamp <= int(i['time']) <= end_timestamp:
            x.append(int(i['time']))
            avg_price = float(i['volumeto']) / float(i['volumefrom'])
            y.append(avg_price)
    # x_mean: the mean of x
    x_mean = sum(x) / len(x)
    # y_mean: the mean of y
    y_mean = sum(y) / len(y)
    # use the formula provided by the professor to calculate the m value
    # num: the numerator of the m value
    num = 0
    # deno: the denominator of the m value
    deno = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        deno += (x[i] - x_mean) ** 2
    m = num / deno
    # use the formula provided by the professor to calculate the b value
    b = y_mean - m * x_mean
    # predict the average price for the next day
    next_day_timestamp = end_timestamp + 86400
    predicted_avg = m * next_day_timestamp + b
    return predicted_avg


# classify_trend(investment) -> str
# investment: Investment type
def classify_trend(investment):
    data, start_date, end_date = investment.data, investment.start_date, investment.end_date
    start_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    # x: the list of time
    x = []
    # y: the list of high price
    y = []
    for i in data:
        if start_timestamp <= int(i['time']) <= end_timestamp:
            x.append(int(i['time']))
            y.append(float(i['high']))
    # x_mean: the mean of x
    x_mean = sum(x) / len(x)
    # y_mean: the mean of y
    y_mean = sum(y) / len(y)
    # Use the formula provided by the professor to calculate the m value
    # num: the numerator of the m value
    num = 0
    # deno: the denominator of the m value
    deno = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        deno += (x[i] - x_mean) ** 2
    m_high = num / deno
    # b is not needed (because we only need to know the trend)
    # x: the list of time
    x = []
    # y: the list of low price
    y = []
    for i in data:
        if start_timestamp <= int(i['time']) <= end_timestamp:
            x.append(int(i['time']))
            y.append(float(i['low']))
    # x_mean: the mean of x
    x_mean = sum(x) / len(x)
    # y_mean: the mean of y
    y_mean = sum(y) / len(y)
    # use the formula provided by the professor to calculate the m value
    # num: the numerator of the m value
    num = 0
    # deno: the denominator of the m value
    deno = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        deno += (x[i] - x_mean) ** 2
    m_low = num / deno
    # predict trend using the definition
    if m_high > 0 and m_low > 0:
        return "increasing"
    if m_high > 0 and m_low < 0:
        return "volatile"
    if m_high < 0 and m_low < 0:
        return "decreasing"
    # all other case, return "other"
    return "other"


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("../cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    x = Investment("01/02/2016", "28/02/2016", data)
    print(classify_trend(x))
