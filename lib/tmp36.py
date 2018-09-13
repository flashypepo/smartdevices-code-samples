'''
class TMP36 temperature  sensor

2019_0911 PePo changed for Pycom micropython
source: https://www.losant.com/blog/how-to-read-the-tmp36-temperature-sensor-with-pycom-and-sigfox
2017_0810 PePo added @property and @threshold.setter
2017_0810 PePo first version
#'''

from micropython import const
from machine import ADC
from time import sleep

class TMP36:
    #resistor value in voltage divider
    _RESISTOR_REF = const(10)

    # attributes:
    # _adc: ADC object corresponding with ADC pin
    #       LoPy4/Exp.board: default P13
    # _sensor = ADC-channel which is attached to TMP36
    # _threshold: temperature value for warnings

    def __init__(self, adc_pin):
        # 2018-0911 adopted for Pycom - added attn
        self._adc = ADC()
        self._adc.vref(1094) # calibration from LDR
        self._sensor = self._adc.channel(pin=adc_pin, attn = ADC.ATTN_11DB)
        self._threshold = 30 #defaut threshold

    # get threshold temperature celsius for temperature warning
    @property
    def threshold(self):
        """returns threshold temperature in Celsius"""
        return self._threshold

    @threshold.setter
    def threshold(self, temperature):
        """set threshold to a temperature in Celsius"""
        #OK: print('threshold=', temperature)
        self._threshold = temperature

    # returns temperature value in Fahrenheit
    # pre-condition: self_value is not None
    def fahrenheit(self):
        """returns temperature in Fahrenheit"""
        return (self.celsius() * 9/5) + 32

    # returns temperature value in Celsius
    # pre-condition: self_sensor is not None
    # this method ALWAYS read data from sensor
    def celsius(self):
        """returns temperature in Celsius"""
        return (self._millivolts - 500.0) / _RESISTOR_REF #Pycom/LoPy4, Huzzah
        #NodeMCU: return (self.value) / _RESISTOR_REF

    # returns temperature value in Kelvin
    # Celsius to Kelvin: T(k) = T(c) + 273.15
    # http://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.htm
    # pre-condition: self_value is not None
    def kelvin(self):
        """returns temperature in Kelvin"""
        return self.celsius() + 273.15

    # get the raw sensor value in milliVolts
    @property
    def _millivolts(self):
        """returns sensor data in millivolts"""
        return self._sensor.voltage()

    # demo run reading T, Ctrl-C to abort
    def demo(self, threshold=30.0, dt=2.0):
        """demo of TMP36 sensor"""
        try:
            self.threshold = threshold # for temperature warnings
            print('class TMP36 demo, threshold={0:0.1f}'.format(self._threshold))
            # start reading and displaying temperature
            while True:
                millivolts = self._millivolts # reading in millivolts
                celsius_temp = self.celsius() # degree Celsius
                fahrenheit_temp = self.fahrenheit() # degree Fahrenheit
                kelvin_temp = self.kelvin() # degree Kelvin
                print('TMP36: millivolts {0:0.1f}\tCelsius {1:0.1f}\tFahrenheit {2:0.1f}\tKelvin {3:0.1f}'.format(millivolts, celsius_temp, fahrenheit_temp, kelvin_temp))

                if celsius_temp > self._threshold:
                    print('T>{0:0.1f}: alert on'.format(self._threshold))

                sleep(dt) #wait > s, see datasheet

        except Exception as ex:
            print(ex)
            print('TMP36 demo interrupted!')

if __name__ == '__main__':
    sensor = tmp36.TMP36('P15')
    sensor.demo(25)
