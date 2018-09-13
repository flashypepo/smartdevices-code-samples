# digital IO
# blinking leds
# 3 LEDS connected to LoPy4
# 2018-0913 Peter demo 2018-0914

''' INFO: pin number mapping on the Expansion board 3.0
from machine import Pin

print('INFO: pin number mapping on the Expansion board 3.0...')
print('G-name -- P-name')
help(Pin.exp_board) # G-names
#'''

# LED demo
# 3 LEDs connected to the Expansion board 3.0
# 2018-0816 PePo

# from module 'machine' import the 'Pin' class
from machine import Pin
'''
Define a LED list on several Pin on the Expansion board 3
2018-0816: 3 LEDS, the Pin objects must be specified as Output,
           use G-names, because that is visible on the Expansion board
#'''
leds = [
    Pin('G28', mode=Pin.OUT),
    Pin('G22', mode=Pin.OUT),
    Pin('G17', mode=Pin.OUT),
]

print(leds)

# define some helper functions...

# leds_on() - all leds on
def leds_on():
    # using traditional loop..
    for led in leds:
        led.value(1)


# leds_off() - all leds off
def leds_off():
    # Pythonian: in one code statement
    [led.value(0) for led in leds]

import time

print('LEDs on...')
leds_on()
time.sleep(2)
leds_off()

# #######################
# Pattern generator
# #######################

##### Model
# A LED is ON (1) or OFF (0).
# A sequence of 1's and 0's specifies
# if a particular LED is ON or OFF

##### Design
# There are n(=3) LEDS, so each sequence step is a list of
# 3 elements.
# Define a function which iterates through each sequence step
# and set LED in ON (1) or OFF (0), accordingly.

# play a cylon light pattern...
def cylon(leds, seq, n):
    '''cylon light pattern on leds according to seq, number of times'''

    # init params
    stepCount = len(seq) # number of sequence elements
    nrLeds = len(leds) # number of LEDS

    stepCounter = 0   # a counter
    stepDir = 1       # step increment
    waitTime = 0.2    # delay between playing a sequence element

    # repeat sequence a number-of-times
    for i in range (n):

        # iterate through the LEDs
        for pinref in range(0, nrLeds):
            led = leds[pinref]  # pickup a led

            # Check if LED should be on or off
            if seq[stepCounter][pinref] != 0:
                led.value(True) # LED on
            else:
                led.value(False) # LED off

        # next step in sequence
        stepCounter += stepDir

        # If we reach the end of the sequence reverse
        # the direction and step the other way
        if (stepCounter == stepCount) or (stepCounter < 0):
            stepDir = stepDir * -1
            stepCounter = stepCounter + stepDir + stepDir

        # Wait before moving on
        time.sleep(waitTime)


# define another helper...
def demo_finished():
    time.sleep(1)
    print('done')
    leds_off()


# specify various cylon patterns in demo-functions
# fixed for 3 LEDs

def cylon_demo1(nr=50):
    seq = []
    seq = list(range(0, 3))  # make a list of 3 elements = number of LEDs
    seq[0] = [1, 0, 0]  # LED1 = ON,  LED2 = OFF, LED3 = OFF
    seq[1] = [0, 1, 0]  # LED1 = OFF, LED2 = ON,  LED3 = OFF
    seq[2] = [0, 0, 1]  # LED1 = OFF, LED2 = OFF, LED3 = ON

    # play the sequence
    cylon(leds, seq, nr)
    # finish demo
    demo_finished()

def cylon_demo2(nr=50):
    # different pattern: a moving LED on...
    seq = []
    seq = list(range(0, 4))
    seq[0] = [1, 0, 0,]
    seq[1] = [1, 1, 0,]
    seq[2] = [0, 1, 1,]
    seq[3] = [0, 0, 1,]

    # play the sequence
    cylon(leds, seq, nr)

    # finish demo
    demo_finished()

def cylon_demo3(nr=50):
    # another pattern: two LEDs from opposite ends
    seq = []
    seq = list(range(0, 2))
    seq[0] = [1, 0, 1]
    seq[1] = [0, 1, 0]

    # play the sequence
    cylon(leds, seq, nr)

    # finish demo
    demo_finished()

# ----

# define show time!!
def cylon_demotime():
    print('cylon demo1...')
    cylon_demo1()

    print('cylon demo2...')
    cylon_demo2()

    print('cylon demo3...')
    cylon_demo3()

# ----
# usage / showtime!
if __name__ == '__main__':
    cylon_demotime()
