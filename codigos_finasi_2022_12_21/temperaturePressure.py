#!/usr/bin/env python

import time
import board
import adafruit_bmp280
from bmp280 import BMP280
from datetime import datetime

def pressure():
    try:
        from smbus2 import SMBus
    except ImportError:
        from smbus import SMBus

    # Initialise the BMP280
    bus = SMBus(1)
    i2c = board.I2C()
    bmp280 = BMP280(i2c_dev=bus)

    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    with open("/home/thestias/Documents/DATA/temperature2.txt", "a+") as f:
        f.write(str(datetime.now())+(", ")+str(temperature) + '\n')
    with open("/home/thestias/Documents/DATA/pressure.txt", "a+") as f1:
        f1.write(str(datetime.now())+(", ")+str(pressure) + "\n")
    print('{:05.2f}*C {:05.2f}hPa'.format(temperature, pressure))
    time.sleep(1)
pressure()
