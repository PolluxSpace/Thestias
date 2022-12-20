from dht11 import dht11
from temperaturePressure import pressure
from temperaturaexterna import exTemp
from relativeAltitude import altitude
import subprocess
import os

while True:
    cmd = 'killall libgpiod_pulsein'
    os.system(cmd)
    dht11()
    pressure()
    exTemp()
    altitude()


































