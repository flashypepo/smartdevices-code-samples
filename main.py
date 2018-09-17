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

# College 2: digital IO, analog IO
use_leds = False  # demo 3-LEDs G28/P12, G22/P11, G17/P10
use_button = False # demo button G10/P23
use_ldr = False # demo analog LDR sensor G13/P16
use_tmp36 = False # demo analog TMP36 sensor G0/P15

# TODO: College 3: SPI (OLED display), PWM (Servo, LED), I2C (example sensor?)
use_spi_oled = False  # demo OLED-SPI display (default)
use_gfx = False       # EXTRA demo for drawing graphics on OLED-display(s)

use_pwm_servo = False # demo PWM to control a servo
use_pwm_led = False   # demo of PWM to control intensity of LED

use_bme280 = False    # demo digital temperature sensor, sensor not in electronic package
use_i2c_oled = False  # demo OLED - I2C, display not in electronic package


# TODO: College 4: Wifi, MQTT?
use_wifi = False   # demo Wifi
use_mqtt = False   # demo MQTT

# TODO: College 5, 6: LoRa / LoRaWAN
use_lorawan = False


# #################################
# Wifi Windesheim network
# #################################
import wifimanager

#print('Creating wifi object with a wificonfig-json ...')
wifi = wifimanager.WifiManager('config/wificonfig_template.json') # TEMPLATE Wifi-WF config

#''' TODO: College 4 include connecting to Wifi
#print('Wifi: connecting to a Wifi network...', use_wifi)
if use_wifi:
    print('Connecting to network ...')
    wifi.connect()
    print('Device IP: {0}'.format(wifi._wlan.ifconfig()[0])) # device IP

    # #################################
    # change password for Telnet, FTP etc.
    # #################################
    print('Updating username and password for telnet/ftp...')
    wifi.change_access('micro', 'python') #change if you want

#END_OF_TODO '''


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


# #################################
# College 3- M2M protocols SPI, I2C, PWM
# 2018-0921 Peter new
# #################################

print('M2M protocol: SPI OLED-display ...', use_spi_oled)
print('M2M protocol: PWM (servo) ...', use_pwm_servo)
print('M2M protocol: PWM (fading lED) ...', use_pwm_led)

print('M2M protocol: I2C OLED-display ...', use_i2c_oled)
print('M2M protocol: I2C BME280 ...', use_bme280)

# #################################
# College 4 - communications: Wifi, MQTT
# 2018-0921 Peter new
# #################################
print('Communications: Wifi ...', use_wifi)
print('Communications: MQTT ...', use_mqtt)

# #################################
# College 5, 6 - communications: LoRa
# 2018-0921 Peter new
# #################################
print('Communications: LoRa ...', use_lorawan)
