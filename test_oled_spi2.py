# digital IO
# Adafruit SSD1306-SPI, 128*32
# 2018-0818 Peter used Radomir Dopieralski's ssd1306_spi module

import ssd1306_spi
from machine import SPI, Pin

#spi = SPI(1, baudrate=20000000)
spi = SPI(0, mode=SPI.MASTER) # use defaults
dc = Pin('P9', Pin.OUT)
cs = Pin('P12', Pin.OUT)
rst = Pin('P8', Pin.OUT) # not used?
oled = ssd1306_spi.Display(spi, dc, cs, width=128, height=32)
#__init__(self, spi, dc, cs=None, width=128, height=64):

#oled = ssd(128, 32, spi, Pin('P9'), Pin('P8'), Pin('P12'))

oled.fb.fill(1)
oled.fb.pixel(64, 32, 0)
oled.update()



def whitescreen():
    oled.fb.fill(1)
    oled.update()


def blankscreen():
    oled.fb.fill(0)
    oled.update()


def messageonscreen(mesg, x, y, refresh=False):
    oled.fb.text(mesg, x, y)
    # if refresh, then show text onscreen
    if refresh == True:
        oled.update()


import time
def demo():
    whitescreen()
    time.sleep(1)

    blankscreen()
    messageonscreen('Welkom Peter', 0,0, True)


print(__name__, 'module loaded')
