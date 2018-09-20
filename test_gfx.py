# demo/test of GFX library
# requires gfx.py in lib-folder
# and an active OLED-display, either SPI or I2C
# source: https://learn.adafruit.com/micropython-displays-drawing-shapes?view=all
# 2018-0821 Peter demo, display object MUST be defined in calle - see createGFX()

import time
import gfx

waittime = 5

# create graphics object - factory method
# use properties of display, add pixel-drawing method of display
# display is either SPI (default) or I2C display.
# and must be defined in caller of the module!!
def createGFX(display):
    graphics = gfx.GFX(display.width, display.height, display.pixel)
    return graphics


# draw a line
def drawlines(display, graphics):
    display.fill(0) # blank screen
    graphics.line(0, 0, display.width,display.height, 1) # draw line from lef-top to bottom-right
    graphics.line(display.width, 0, 0, display.height, 1) # draw line from lef-top to bottom-right
    display.show() # show it
    time.sleep(waittime)


# draw rectangles
def drawrectangles(display, graphics):
    display.fill(0) # blank screen
    graphics.rect(0, 0, 60, 15, 1) # draw rectangle
    graphics.fill_rect(65, 18, 65+20, 18+12, 1) # draw filled rectangle
    display.show() # show it
    time.sleep(waittime)


# draw circles
def drawcircles(display, graphics):
    display.fill(0) # blank screen
    graphics.circle(15, 15, 15, 1) # draw filled circle
    graphics.fill_circle(60, 15, 15, 1) # draw filled circle
    display.show() # show it
    time.sleep(waittime)


# draw triangles
def drawtriangles(display, graphics):
    display.fill(0) # blank screen
    graphics.triangle(0, 20, 32, 10, 64, 20, 1)
    graphics.fill_triangle(32, 25, 76, 10, 118, 25, 1)
    display.show() # show it
    time.sleep(waittime)


def demo(display, dt=5):
    waittime = dt # time in seconds between draw-functions
    graphics = createGFX(display) # create graphics object for display

    # demos'
    drawlines(display, graphics)
    drawrectangles(display, graphics)
    drawcircles(display, graphics)
    drawtriangles(display, graphics)


print(__name__, 'is loaded')
