# PWM: pulsing LED
# 2018-0920 Peter

import math, time
from machine import PWM

class PulseLED(object):
    """pulsing LED"""
    def __init__(self, pin, freq=1000, timer=0):
        #super(, self).__init__()
        self.pwm = PWM(timer, frequency=freq)
        self.led_c = self.pwm.channel(0, pin=pin, duty_cycle=0)

    # pulse function
    def pulse(self, t):
        """pulse led l with time interval t in ms"""
        for i in range(17):
            self.led_c.duty_cycle( math.sin( i / 10 * math.pi ))
            time.sleep_ms(t)


if __name__ == '__main__':
    # LED configuration:
    # blauwe LED on GPIO7 ('P20')
    led_pin = 'P20'
    led = PulseLED(pin=led_pin)
    for i in range(50):
        led.pulse(20)
