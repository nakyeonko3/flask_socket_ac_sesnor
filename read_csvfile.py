import pandas as pd
import re

def get_senor_data_last_value():
    df = pd.read_csv('sensor.csv')
    last_number = df['Sensor'].values[-1]
    last_Date = df['Date'].values[-1]
    return int(last_number)
    #csv file 마지막 줄의 Sensor 값을 가져옴

def get_date_last_value():
    df = pd.read_csv('sensor.csv')
    last_Date = df['Date'].values[-1]
    return int(last_Date) 
    #csv file 마지막 줄의 Date 값을 가져옴


def get_last_line():
    with open('sensor.csv', "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
    final_line = re.sub(r'[^0-9]', '', final_line)
    return final_line
    #csv 마지막줄다 가져옴

if __name__ == "__main__":
    #print(read_csv_Date_value_last())
    # print(read_csv_Sensor_value_last())
    print(int(get_senor_data_last_value()))

    # string = 'aaa1234, ^&*2233pp'
    # numbers = re.sub(r'[^0-9]', '', string)
    # print(numbers)


