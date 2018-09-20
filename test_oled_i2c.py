# digital IO
# Adafruit SSD1306-I2C, 128*32
# 2018-0821 Peter
# problem: SPI and I2C share common Pin 'P8' for CLK
#

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C as ssd


#i2c = I2C(0, mode=I2C.MASTER) # use defaults
# The default I2C pins are P9 (SDA) and P10 (SCL)
i2c = I2C(0, I2C.MASTER, baudrate=100000,pins=("P9", "P8"))
print('i2c scan:', i2c.scan())

# create OLED object
oled = ssd(128, 32, i2c) # default addr = 0x3c
#oled.fill(1)
#oled.show() # should give white screen


def whitescreen():
    oled.fill(1)
    oled.show()


def blankscreen():
    oled.fill(0)
    oled.show()


def messageonscreen(mesg, x, y, refresh=False):
    oled.text(mesg, x, y)
    # if refresh, then show text onscreen
    if refresh == True:
        oled.show()


import time

def messagescroll(dx, dy, dt, refresh=True):
    oled.scroll(dx, dy)
    if refresh == True:
        oled.show()


def demo(s1, s2 = 'Welkom!!'):
    whitescreen()
    time.sleep(1)

    blankscreen()
    messageonscreen(s2, 0, 0, False)
    messageonscreen(s1[:15], 0, 13, False)
    messageonscreen(s1[15:], 0, 23 , True)

print(__name__, 'module loaded')
