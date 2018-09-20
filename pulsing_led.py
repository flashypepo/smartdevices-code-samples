# PWM: pulsing LED
# 2018-0920 Peter

import machine, math, time

# LED configuration
#led_pin = 'P0' # yellow led - GPIO2
led_pin = 'P20' # blue led - GPIO7

pwm = machine.PWM(0, frequency=1000)
led = pwm.channel(0, pin=led_pin, duty_cycle=0)

# pulse function
def pulse(l, t):
    """pulse led l with time interval t in ms"""
    for i in range(17):
        l.duty_cycle( math.sin( i / 10 * math.pi ))
        time.sleep_ms(t)


if __name__ == '__main__':
    print('Demo pulsing LED...')
    for i in range(50):
        #''' pulse LED
        pulse(led, 50)
