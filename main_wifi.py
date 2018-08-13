# main.py
# 1. connect to Wifi - Windesheim
# 2. change server password

import micropython
# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

# #################################
# Wifi Windesheim network
# #################################
import wifimanager

print('Connecting to network in wificonfig.json...')
wifi = wifimanager.WifiManager("wificonfig.json")
params = wifi.connect()
print('Device IP is {0}'.format(params[0])) # device IP


# #################################
# change password for Telnet, FTP etc.
# #################################
print('Updating username and password for telnet/ftp...')
wifi.change_access('micro', 'python') #change if you want

# #################################
# show MAC-address
# #################################
print('MAC-adres:', wifi.mac)
