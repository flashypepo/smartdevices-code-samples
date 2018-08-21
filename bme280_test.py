"""
test BME280 temperature sensor on LoPy4
2018-0821 use BME280_2 library (requires: Devices, SensorConstants)
"""

import time
from machine import I2C
import BME280_2

# I2C on LoPy4 uses SDA=P9, SCL=P8
i2c = I2C(0, I2C.MASTER, baudrate=100000,pins=("P9", "P8"))
print('i2c scan:', i2c.scan())

#create bme sensor object
bme = bme280_2.BME280(i2c=i2c)#default:, addr=i2c.scan()[0])
print('bme:', bme)

# print T, P, and H
while(True):
    t = bme.temperature()
    p = bme.pressure
    h = bme.humidity
    data = (bme.temperature, bme.pressure, bme.humidity)
    print(data)
    time.sleep(2)
