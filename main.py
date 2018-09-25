# main.py - development
# 1. connect to Wifi - Windesheim
# 2. change server password
# 2018-0920 Peter - added College 3 samples
# 2018-0917 Peter - added import time, College 3-5 devices-flags
# 2018-0913 Peter - cleaning up for digitalIO and analogIO
# 2018-0906 Peter - comment connecting network
# 2018-0814 Peter - displays only MAC-address

import time
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

# College 3: SPI (OLED display), PWM (Servo, LED), I2C (example sensor?)
use_spi_oled = False  # demo OLED-SPI display (default)
use_i2c_oled = False  # demo OLED - I2C, display not in electronic package
use_bme280 = False    # demo digital temperature sensor, sensor not in electronic package
use_gfx = False       # EXTRA demo for drawing graphics on OLED-display(s)

use_pwm_servo = False # demo PWM to control a servo
use_pwm_led = False   # demo of PWM to control intensity of LED


# TODO: College 4: Wifi, MQTT?
use_wifi = True   # connect to Wifi
use_mqtt = False   # demo MQTT

# TODO: College 5, 6: LoRa / LoRaWAN
use_lorawan = False


# #################################
# Wifi Windesheim network
# #################################
import wifimanager

print('Creating wifi object with a wificonfig-json ...')
#wifi = wifimanager.WifiManager('config/wificonfig_template.json') # WF plceholder config
#myWF: wifi = wifimanager.WifiManager('config/wificonfig.json') # WF config
wifi = wifimanager.WifiManager('config/wificonfig_home.json') # HOME
#TODO: wifi = wifimanager.WifiManager('wificonfig.json') # SAMPLE Wifi-WF config
#print('TODO EXERCISE: include connecting to Wifi...')

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
# 2018-0907 MAC-address ook te zien
# als Device ID tijdens firmware upgrade
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

    except KeyboardInterrupt:
        print('LED cyclon demo done')

print('digital IO: button - LED demo...', use_button)
if use_button:
    import buttondemo
    #buttondemo.test1() # no debounce
    buttondemo.test2() # debounce

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
        sensor = tmp36.TMP36('P15')
        sensor.demo(25)

    except KeyboardInterrupt:
        print('TMP36 demo done')


# LDR: ambient light sensor
# use flash light of smartphone for light variations
print('analog IO: LDR readings...', use_ldr)
if use_ldr:
    print('LDR on Pin...', 'P16 (GPIO3)')

    try:
        import lightsensor

        # simple test
        #lightsensor.test1()

        # simple light meter with LEDs
        lightsensor.lightmeter()

    except KeyboardInterrupt:
        print('LDR demo done')


# #################################
# Experiment: OLED 128*32 SPI and I2C
# 2018-0821 added OLED-I2C and OLED-SPI
# 2018-0819 okay with ssd1306 of DiCola
# #################################
print('Communications: SPI OLED-display...', use_spi_oled)
if use_spi_oled:
    from test_oled_spi import demo
    demo(wifi.mac)

print('Communications: I2C OLED-display...', use_i2c_oled)
if use_i2c_oled:
    from test_oled_i2c import demo
    demo(wifi.mac)

# showtime...
time.sleep(3)

print('graphics ...', use_gfx)
if use_gfx and use_spi_oled:
    from test_oled_spi import oled as display
    from test_gfx import demo
    demo(display)

if use_gfx and use_i2c_oled:
    from test_oled_i2c import oled as display
    from test_gfx import demo
    demo(display)

# showtime...
time.sleep(3)

# #################################
# Experment: BME280, I2C temperature sensor
# 2018-0821: requires i2c from test_oled_i2c
# TODO WISH: separate classes for I2C_BUS and SPI_BUS objects
# #################################
print('Communications: I2C digital sensor BME280...', use_bme280)
if use_bme280:
    from test_oled_i2c import i2c

    # Select display either SPI and/or I2C ...
    if use_spi_oled:
        from test_oled_spi import oled as display

    else:
        from test_oled_i2c import oled as display


    import test_bme280
    test_bme280.demo(i2c, display, 2)


# #################################
# Experiment PWM: servo, pulsing led
# #################################
print('Communications: PWM ... servo: ', use_pwm_servo)
if use_pwm_servo:
    # non-OOP version, using directly PWM
    # Servo: GPIO6 / 'P19' Expansion board
    # Vcc = 5V, signal=3V3 (GPIO)
    from test_servo import demo
    demo()

    # TODO OOP version


print('Communications: PWM ... LED: ', use_pwm_led)
if use_pwm_led:
    # LED configuration
    #led_pin = 'P0' # yellow led - GPIO2
    led_pin = 'P20' # blue led - GPIO7

    ''' non-OOP version
    from pulsing_led import led, pulse
    for i in range(50):
        pulse(led, 20)
    '''
    # OOP version - see lib-folder
    from pulseled import PulseLED
    led = PulseLED(pin=led_pin)
    for i in range(30):
        led.pulse(20)
    #'''

# #################################
# College 4 - communications: Wifi, MQTT
# 2018-0921 Peter new
# #################################
print('Communications: Wifi ...', use_wifi)
if use_wifi and wifi.isconnected:
    from get_webpage import http_get

    # demo: get a (small) test webpage
    print('\n== DEMO#1: getting test webpage...')
    http_get('http://micropython.org/ks/test.html', 80) #test page

    # demo: get the UTC-time
    # Note: does not work al the time
    print('\n\n== DEMO#2: getting the UTC time...')
    http_get('http://time-a.nist.gov/', 13)

    # demo: get your public IP
    print('\n\n== DEMO#3: getting public IP...')
    http_get('http://ip.jsontest.com/', 80) # JSON file

print('Communications: MQTT ...', use_mqtt)

# #################################
# College 5, 6 - communications: LoRa
# 2018-0921 Peter new
# #################################
print('Communications: LoRa ...', use_lorawan)
