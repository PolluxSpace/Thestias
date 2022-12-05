import serial              
from time import sleep
import sys

ser = serial.Serial ('/dev/ttyS0',9600)
try:
    while True:
        received_data = (str)(ser.readline()) #read NMEA string received
        print(received_data)
        print("")
except KeyboardInterrupt:
    sys.exit(0)  