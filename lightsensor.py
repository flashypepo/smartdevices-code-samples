# lightsensor.py - demo of LDR lightsensor
#
# ATTENTION from the pycom documentation (firmware):
# ADC pin input range is 0-1.1V. This maximum value can
# be increased up to 3.3V using the highest attenuation of 11dB.
#
# 2018-0911 Peter new, read the firmware documentation too!!
# source:
# 1. Tutorial: https://docs.pycom.io/tutorials/all/adc
# 2. Firmware: https://docs.pycom.io/firmwareapi/pycom/machine/adc

from machine import ADC
adc = ADC()

# calibration - see Pycom documentation
#adc.vref_to_pin('P6') # only P6, P21, P22 can be used.
#
# a reference voltage of 1.1V is on Pin,
# measure a value with a multimeter,
# For example my measured value was 1094 mV.
# This will be calibrated value for adc.vref(value)
# After reading value on multimeter:
# 1. RESET the board!!
# 2. comment the code adc.vref_to_pin('P6')

# set calibration
adc.vref(1094)

# lightsensor is connected to GPIO3 / P16
# create an ADC-channel, use highest attenuation of 11dB
# (ADC.ATTN_11DB) in order to use 3V3 input.
# https://docs.pycom.io/firmwareapi/pycom/machine/adc
ldr = adc.channel(pin='P16', attn=ADC.ATTN_11DB)

# test lightsensor: reading values
from time import sleep

def test1():
    while True:
        print('light={} mV'.format(ldr.voltage()))
        sleep(1)

# simple lightmeter

#TODO: put code for lightmeter here....
# Use methods, like leds_off(), and leds-array from module leds


if __name__ == '__main__':
    try:
        # use flash light of smartphone
        test1()
        #TODO: lightmeter()

    except KeyboardInterrupt:
        print('done')
