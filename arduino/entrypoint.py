import time

import serial


# Открываем последовательный порт
ser = serial.Serial('COM6', 9600)


def receive():
    data = ser.readline().decode()

    # -----------
    #
    # Проверка полученных данных из локальной базы данных.
    #
    # -----------

    # -----------
    #
    # Отправка данных по API.
    #
    # -----------


while True:
    time.sleep(2)
    receive()
