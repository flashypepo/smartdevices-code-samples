# MicroPython for the IOT - Chapter 11
#
# Project 4: MicroPython Weather Node
#
# Required Components:
# - BME280 Weather Sensor
##
# 2018-0926 Peter - adopted for Adafruit IO credentials,
#           - removed Wifi connection - is precondition
#
# Imports for the project
from network import WLAN
from weather_node import WeatherNode
import machine

# Define out user id and key
_IO_ID = "YOUR_DEVICE_ID" # Peter: can be any string,
_IO_USERNAME ="YOUR AOI USERNAME"
_IO_KEY = "YOUR AIO key"
_FREQUENCY = 5 # seconds

# 2018--0927 Peter: added i2c, because it alsready exists.
def run(i2c_inUse):
    # Setup our Internet connection
    #2018-0926 PePo removed: connect()

    # Run the weather MQTT client
    weather_mqtt_client = WeatherNode(i2c_inUse, _IO_ID, _IO_USERNAME, _IO_KEY, _FREQUENCY)
    weather_mqtt_client.run()
