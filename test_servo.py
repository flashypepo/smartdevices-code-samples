# test_servo
# 2018-0920 Peter new, non-OOP versie, using directly PWM
# Sources:
# 1. Pycom documentatie: https://docs.pycom.io/firmwareapi/pycom/machine/pwm
# 2. frequency parameter and pulse LED:
# http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/pwm.html#control-a-hobby-servo

from time import sleep
from machine import PWM

# Servo configuration: GPIO6 / 'P19' Expansion board
# Vcc = 5V, signal=3V3 (GPIO)
# Servo type TG9e - assortimentsdoos
# trial-and-error values
duty_range = [0.025, 0.05]

pwm = PWM(0, frequency=50) #servo: frequency = 50 Hz
duty_mean = (duty_range[0] + duty_range[1]) / 2
servo = pwm.channel(0, pin='P19', duty_cycle=duty_mean)

def sweep(min_duty, max_duty, dt = 2):
    """ sweep servo between min_duty and max_duty and waittime dt. """
    while True:
        servo.duty_cycle(min_duty) # one side
        sleep(dt)
        servo.duty_cycle(max_duty) # other side
        sleep(dt)


# demo: sweep the servo...
def demo():
    """ demo sweep servo until Ctrl-C."""
    try:
        sweep(duty_range[0], duty_range[1], 2)

    except KeyboardInterrupt:
        servo.duty_cycle(duty_mean)
