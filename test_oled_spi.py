# digital IO
# Adafruit SSD1306-SPI, 128*32
# 2018-0818 Peter
# problem: https://forum.pycom.io/topic/3655/ssd1306-with-spi-on-lopy4-topic-1541-solved-ssd1306-with-spi-on-wipy

from machine import Pin, SPI
from ssd1306 import SSD1306_SPI as ssd

#spi = SPI(0, mode=SPI.MASTER, baudrate=8000000, polarity=0, phase=0)
spi = SPI(0, mode=SPI.MASTER) # use defaults

dc_pin  = Pin('P9') # G16
rst_pin = Pin('P8') # G15
cs_pin  = Pin('P12')# G28

#oled = ssd(128, 32, spi, dc, rst, cs)
#oled = ssd(128, 32, spi, Pin('P9'), Pin('P8'), Pin('P12'))
#OK: oled = ssd(128, 32, spi, dc_pin, rst_pin, cs_pin)
oled = ssd(128, 32, spi, Pin('P9'), Pin('P8'), Pin('P12'))
# 2018-0819 TypeError: function expected at most 5 arguments, got 6
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
    messageonscreen(s1[15:], 0, 23, True)


print(__name__, 'module loaded')
