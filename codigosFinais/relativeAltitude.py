#!/usr/bin/env python

import time
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

def altitude():

    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)

    baseline_values = []
    baseline_size = 100

    print("Collecting baseline values for {:d} seconds. Do not move the sensor!\n".format(baseline_size))

    for i in range(baseline_size):
        pressure = bmp280.get_pressure()
        baseline_values.append(pressure)
        time.sleep(1)

    baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])

    altitude = bmp280.get_altitude(qnh=baseline)
    with open("/home/thestias/Documents/DATA/altitude.txt", "a+") as f:
        f.write(str(altitude)+"\n")
    print('Relative altitude: {:05.2f} metres'.format(altitude))
    time.sleep(1)
