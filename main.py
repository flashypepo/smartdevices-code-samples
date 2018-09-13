# main.py - sample
# 1. connect to Wifi - Windesheim
# 2. change server password
# 2018-0911 Peter added cylon LED pattern demo
# 2018-0820 Peter - OMG no crednetials online using GitHub
# 2018-0814 Peter - displays only MAC-address

import micropython
# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

# used devices in main:

# TODO: College 2: digital IO, analog IO
use_leds = True  # demo 3-LEDs G28/P12, G22/P11, G17/P10
use_button = True # demo button G10/P23
use_ldr = True # demo analog LDR sensor G13/P16
use_tmp36 = True # demo analog TMP36 sensor G0/P15


# #################################
# Wifi Windesheim network
# #################################
import wifimanager

print('Creating wifi object with a wificonfig-json ...')
wifi = wifimanager.WifiManager('config/wificonfig_template.json') # TEMPLATE Wifi-WF config

''' TODO: include connecting to Wifi
print('Connecting to network ...')
wifi.connect()
print('Device IP: {0}'.format(wifi._wlan.ifconfig()[0])) # device IP


# #################################
# change password for Telnet, FTP etc.
# #################################
print('Updating username and password for telnet/ftp...')
wifi.change_access('micro', 'python') #change if you want

#END_OF_TODO '''

print('TODO: EXERCISE: include connecting to Wifi...')

# #################################
# show MAC-address
# 2018-0907: MAC-address is also shown during
# firmware upgrade as Device ID.
# #################################
print('MAC-adres:', wifi.mac)


# #################################
# College 2- digital IO
# - cylon LED patterns
# - button-LED demo
# 2018-0911 Peter new
# #################################
print('digital IO: cylon patterns...', use_leds)
if use_leds:
    try:
        import leds
        leds.cylon_demotime()

        # TODO: your code in lib/leds.py for a knight-rider pattern

    except KeyboardInterrupt:
        print('LED cyclon demo done')

print('digital IO: button demo...', use_button)
if use_button:
    import buttondemo
    buttondemo.test1() # naive solution, no debounce

    #  TODO: Your code in buttondemo.py for button debounce

    print('Button demo done')

# #################################
# College 2- analog IO
# - LDR lightsensor
# - TMP36 temperature sensor
# 2018-0911 Peter new
# #################################

# TMP36: ambient temperature sensor
print('analog IO: TMP36 readings...', use_tmp36)
if use_tmp36:
    print('TMP36 on Pin...', 'P15 (GPIO0)')
    try:
        import tmp36

        # TODO: add your code to add a TMP36 sensor

    except KeyboardInterrupt:
        print('TMP36 demo done')


# LDR: ambient light sensor
# use flash light of smartphone for light variations
print('analog IO: LDR readings...', use_ldr)
if use_ldr:
    print('LDR on Pin...', 'P16 (GPIO3)')

    try:
        import lightsensor

        # TODO: add your code in lightsensor.py for a simple lightmeter

    except KeyboardInterrupt:
        print('LDR demo done')
