# main.py
# 1. connect to Wifi - Windesheim
# 2. change server password
# 2018-0814 Peter - displays only MAC-address

import micropython
# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

# #################################
# Wifi Windesheim network
# #################################
import wifimanager

print('Creating wifi object with a wificonfig-json ...')
wifi = wifimanager.WifiManager() # default JSON file
print('EXERCISE: include connecting to Wifi...')
''' TODO: include connecting to Wifi
print('Connecting to network ...')
wifi.connect()
print('Device IP: {0}'.format(wifi._wlan.ifconfig()[0])) # device IP


# #################################
# change password for Telnet, FTP etc.
# #################################
print('Updating username and password for telnet/ftp...')
wifi.change_access('micro', 'python') #change if you want
'''

# #################################
# show MAC-address
# #################################
print('MAC-adres:', wifi.mac)