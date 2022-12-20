import time
import board
import digitalio
import adafruit_max31855

def exTemp():

    spi = board.SPI()
    cs = digitalio.DigitalInOut(board.D5)
    max31855 = adafruit_max31855.MAX31855(spi, cs)

    tempC = max31855.temperature
    #tempF = tempC * 9 / 5 + 32
    print("Temperature: {} C".format(tempC))
    with open("/home/thestias/Documents/DATA/extemp.txt", "a+") as f:
        f.write(str(tempC)+"\n")
    time.sleep(1.0)