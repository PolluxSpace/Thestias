import time
import board
import adafruit_mpu6050
import math

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    print("Acceleration: X:%.2f, Y:%.2f, Z:%.2f m/s²" % (mpu.acceleration))
    print("Gyro X:%.2f, Y:%.2f, Z:%.2f rad/s" % (mpu.gyro))
    ang = Math.cos^-1("x:%.2f"% (mpu.acceleration))
    print(ang)
    
    time.sleep(1)
    