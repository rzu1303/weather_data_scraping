import psycopg2
import w_data
from PyQt5 import QtCore
from datetime import date
from pprint import pprint
import queue
from datetime import datetime
import itertools
import csv
import config


def read_weather(city, start_date, end_date):
    icity = city 
    istart_date = start_date
    iend_date = end_date

    date1 = datetime.strptime(iend_date, '%Y-%m-%d')
    date2 = datetime.strptime(istart_date, '%Y-%m-%d')
    time_difference = date1 - date2
    number_of_days = time_difference.days
    number_of_days = number_of_days + 1

    ## Creating link
    # website = "https://www.visualcrossing.com/weather/weather-data-services/dhaka/metric/2023-05-28/2023-06-01"
    
    base_url = "https://www.visualcrossing.com/weather/weather-data-services/"
    city = icity
    start_date = istart_date
    end_date = iend_date

    link = f"{base_url}{city}/metric/{start_date}/{end_date}"

    global data_ex
    data_ex = queue.Queue()
    data_q = queue.Queue(maxsize=number_of_days)

    data_q = w_data.read_weather(link,number_of_days)

    for item in list(data_q.queue):
        data_ex.put(item)

    return (data_q,number_of_days)



def write_weather():
    ###### list
    # with open("Weather_data.csv", "a", encoding="utf-8") as fp:
    #     for index in range(0, len(temp), 1):
    #         fp.write(temp[index]+","+" "+ humi[index]+","+prec[index]+","
    #                 +","+wind[index]+"\n")
    ##### queue  ####need to be tested#####

    with open("Weather_data_test1.csv", "w", encoding="utf-8") as fp:   
        writer = csv.DictWriter(fp, fieldnames=["temperature", "humidity", "precip", "wind"])
        writer.writeheader()
        while not data_ex.empty():

            data = data_ex.get()
            writer.writerow(data)

            
        print("data saved in csv file")


if __name__=="__main__":
    pass
