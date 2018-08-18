from machine import Pin

# button: G16 on Expansion baord
button = Pin(Pin.exp_board.G16, mode=Pin.IN, pull=Pin.PULL_UP)
leds = [
    Pin('G28', mode=Pin.OUT),
    Pin('G22', mode=Pin.OUT),
    Pin('G17', mode=Pin.OUT),
]
def leds_on():
    for led in leds:
        led.value(1)

def leds_off():
    for led in leds:
        led.value(0)


def test1():
    while True:
        if button.value() == 0:
            print('presssss !!!!')
            #leds_on()
        #else:
            #leds_off()


#print ('Test1...')
#test1()

# debounce oplossing
import time
def test2():
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second:
            print('button pressed!')
            leds_on()
        elif not first and second:
            print('button released!')
            leds_off()


print ('Test2...')
test2()
