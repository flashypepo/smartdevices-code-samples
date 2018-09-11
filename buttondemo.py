# buttondemo - demonstration of button (non-debounced)
# 2018-0911 Peter new

from machine import Pin
from leds import leds_on, leds_off

# button: G10 on Expansion baord
# button open/nominal: GPIO-pin is LOW (connected to GND)
# button closed/pressed: GPIO-pin becomes HIGH (connected to 3V3)
# Note: Tony DiCola's article is the other way
#       button open/nominal: GPIO-pin is HIGH (1)
#       button closed/pressed: GPIO-pin is LOW (0)
button = Pin(Pin.exp_board.G10, mode=Pin.IN)

# test1() - naive button detection
def test1():
    leds_off()
    while True:
        if button.value() == 1:
            print('presssss !!!!')
            leds_on()
        else:
            # button is in open state
            leds_off()

# debounce oplossing
# Opdracht

if __name__ == '__main__':
    print('digital IO: button - LED demo...')
    import buttondemo
    # to debounce or not to debounce
    print('test1')
    buttondemo.test1() # no debounce
