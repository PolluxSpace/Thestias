import time
import board
import adafruit_dht
import psutil

def dht11():    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
           proc.kill()
    sensor = adafruit_dht.DHT11(board.D23)
    count = 1
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        with open("/home/thestias/Documents/DATA/temperature.txt", "a+") as f:
            f.write(str(count)+(", ")+str(sensor.temperature)+"\n")
        count += 1
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(1.0)

