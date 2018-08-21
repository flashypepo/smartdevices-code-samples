# main.py
# 1. connect to Wifi - Windesheim
# 2. change server password
# 2018-0820 Peter - OMG no crednetials online using GitHub
# 2018-0814 Peter - displays only MAC-address

import micropython
# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

# used devices in main:
use_oled_spi = True
use_oled_i2c = True
use_bme280 = True


# #################################
# Wifi Windesheim network
# #################################
import wifimanager

print('Creating wifi object with a wificonfig-json ...')
wifi = wifimanager.WifiManager('config/wificonfig_home.json') # HOME config
#TODO: wifi = wifimanager.WifiManager('wificonfig.json') # SAMPLE Wifi-WF config
#print('EXERCISE: include connecting to Wifi...')

#''' TODO: include connecting to Wifi
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
# #################################
print('MAC-adres:', wifi.mac)

# #################################
# Experment: OLED 128*32 SPI and I2C
# 2018-0821 added OLED-I2C
# 2018-0819 okay with ssd1306 of DiCola
# #################################
if use_oled_spi:
    import test_oled_spi
    test_oled_spi.demo(wifi.mac)

if use_oled_i2c:
    import test_oled_i2c
    test_oled_i2c.demo(wifi.mac)

# #################################
# Experment: BME280, I2C temperature sensor
# 2018-0821: requires i2c from test_oled_i2c
# TODO WISH: separate classes for I2C_BUS and SPI_BUS objects
# #################################
if use_bme280:
    from test_oled_i2c import i2c

    # Select display either I2C or SPI...
    # Toggle '#' on next line
    ''' use OLED-I2C display
    from test_oled_i2c import oled as display
    '''
    #use OLED-SPI display
    from test_oled_spi import oled as display
    #'''

    import test_bme280
    test_bme280.demo(i2c, display, 2)
