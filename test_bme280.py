'''
  test a MBE280/BMP280 temperature  sensor
  pin sensor  LoPy4
  SCL         P8 / G15
  SDA         P9 / G16
  VIN         3.3V
  GND         GND

#'''
from micropython import const
import machine
import time
import json
import bme280   #required in lib-folder

# helper function: Celsius to Fahrenheit
# Exercise 2018: requires temperature as raw value from bme20 module. Change library.
def fahrenheit(celsius):
    return (celsius * 9/5) + 32

bme = None # placeholder for a bme280 object

# create a bme280 object
def createBME280(i2c_inuse):
    return bme280.BME280(i2c=i2c_inuse)

def bme2json():
    dict = {} # store data in dict
    dict['temp'] = bme.values[0]
    #print(dict['temp'])
    dict['pressure'] = bme.values[1]
    #print(dict['pressure'])
    dict['humidity'] = bme.values[2]
    #print(dict['humidity'])
    #dict['internal'] = machine.internal_temp()[1] #ESP32 temperature sensor
    return json.dumps(dict) #JSON format

# run sensor reading, Ctrl-C to abort
def demo(i2c, display=None, dt=2.0):
    global bme
    try:
        bme = createBME280(i2c)
        while True:
            print('BME280 values: ', bme.values)
            print('JSON:', bme2json())

            if display is not None:
                t, p, h = bme.values
                display.fill(0)
                display.text('Temp: {:}'.format(t), 0, 0)
                display.text('Pres: {:}'.format(p), 0, 13)
                display.text('Hum: {:}'.format(h), 0, 23)
                display.show()

            time.sleep(dt) #wait > s, see datasheet

    except Exception as ex:
        print(ex) # show exception message
        print('done')


print(__name__, 'module loaded')
