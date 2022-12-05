import time
import board
import digitalio
import adafruit_max31855

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)

max31855 = adafruit_max31855.MAX31855(spi, cs)
while True:
    tempC = max31855.temperature
    #tempF = tempC * 9 / 5 + 32
    print("Temperature: {} C".format(tempC))
    time.sleep(2.0)