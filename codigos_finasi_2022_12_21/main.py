from dht11 import dht11
from temperaturePressure import pressure
from temperaturaexterna import exTemp
from relativeAltitude import altitude
from gps_final import gps
from altitudeStart import altitudeStart
import subprocess
import os

baseline_values = altitudeStart()

while True:
    cmd = 'killall libgpiod_pulsein'
    os.system(cmd)
    dht11()
    gps()
    pressure()
    exTemp()
    altitude(baseline_values)


































