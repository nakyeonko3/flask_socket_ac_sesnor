import time
import pandas as pd
from datetime import datetime

df = pd.DataFrame([], columns=['Date', 'Sensor'])


import socket
import time

port = 8888
address = ("192.168.9.218", port)
# address = ("192.168.1.114", port)
BUFSIZE = 512

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

ac_sensor_data = 0


def receve_data_from_sock_sever():
    while True:
        data = s.recv(BUFSIZE) #receive message from server
        if data == "":
            break
        make_csvfile(data.decode()) 

def make_csvfile(sensor_value):
    global df
    new_line = pd.DataFrame({
            'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'Sensor': [sensor_value]
            })
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv('sensor.csv', index=False)


if __name__ == "__main__":
    receve_data_from_sock_sever()



