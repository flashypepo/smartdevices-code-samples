#
"""
wifimanager.py - connects to Wifi networks
* Micropython: Pycom uP
* static or dynamic IP
* JSON-based
2018-0528 PePo adopted to pycom. add mac-address

Format 'wificonfig.json':
{
    "STATIC_IP": "None",            # or, "145.45.16.2" for STATIC IP
    "SUBNET" : "your subnet IP",    # example: "192.168.178.0"
    "GATEWAY_IP": "your gateway IP",# example: "192.168.178.1"
    "MASKER": "your mask",          # example: "255.255.255.0",
    "SSID": "your ssid",            # example: "PePoDevNet"
    "PASSWRD" : "your password",
    "DNS": "8.8.8.8"                # example Google DNS
    "IDENTITY": "device id"         # kind of device id, its name
}
"""

#pycom:
from network import WLAN, Server
import machine
import json
from ubinascii import hexlify

# configurations
USE_DEBUG = True   # DEBUG or not debug


class WifiManager:

    def __init__(self, jsonfile="wificonfig.json"):
        # Load configuration from config JSON file.
        # wificonfig.json contans the network settings
        # STATIC_IP is 'None' or empty string -> use dynamic IP
        self._config = self.readjson(jsonfile)

        #create network in STAtion mode
        #pycom: device always starts up in AP-mode
        self._wlan = WLAN(mode=WLAN.STA)
        if USE_DEBUG:
            print('WifiManager::WLAN mode:', self._wlan.mode()) #pycom: 1=STA, 2=AP)

    def readjson(self, jsonfile):
        """readjson(file) - returns the contents of file in JSON-format"""
        with open(jsonfile, 'r') as infile:
            config = json.load(infile)
        if USE_DEBUG:
            print ('WifiManager::JSON settings: {}'.format(config))
        return config

    # pycom connect
    def connect(self):
        """connect() - connects device according to network parameters in JSON-file."""
        self._wlan = WLAN() # get current object, without changing the mode

        # skip connecting, when a soft-reset is performed
        if machine.reset_cause() != machine.SOFT_RESET:
            self._wlan.init(mode=WLAN.STA)
            # configuration below MUST match your home router settings!!
            # IP, Subnet, Gateway, DNS
            if self._config['STATIC_IP'] != None:
                if USE_DEBUG:
                    print('WifiManager::Static IP configuration for SSID ', self._config['SSID'])

                self._wlan.ifconfig(config=(self._config['STATIC_IP'], self._config['MASKER'], self._config['GATEWAY_IP'], self._config['DNS']))

            # connect to Wifi
            if USE_DEBUG:
                print('WifiManager::isconnected:', self._wlan.isconnected())

            if not self._wlan.isconnected():
                if USE_DEBUG:
                    print("WifiManager::start MAC '{0}' to connect to '{1}' with IP '{2}'".format(self.mac, self._config['SSID'], self._config['STATIC_IP']))

                # change the line below to match your network ssid, security and password
                self._wlan.connect(self._config['SSID'], auth = (WLAN.WPA2, self._config['PASSWRD']), timeout = 5000)
                while not self._wlan.isconnected():
                    machine.idle() # save power while waiting

        # connected, return network config
        return self._wlan.ifconfig()

    # wrapper for disconnecting network
    def disconnect(self):
        """disconnect() - de-activate network interface, but leaves Wifi radio on"""
        self._wlan.disconnect() # pycom - disconnect from Wifi, but leave Wif radio on.
        if USE_DEBUG:
            print('WifiManager::WLAN connected:', self._wlan.isconnected()) # DEBUG

    # wrapper for disabling Wifi radio
    def deinit(self):
        """deinit() - disable Wifi radio"""
        self._wlan.deint() # pycom
        if USE_DEBUG:
            print('WifiManager::Wifi radio off')

    # wrapper for network scan
    def scan(self):
        """scan() - Performs a network scan and returns a list
        of named tuples with (ssid, bssid, sec, channel, rssi)
        """
        return self._wlan.scan()

    # wrapper for wlan.isconnected()
    @property
    def isconnected(self):
        """isconnected() - returns if connected to Wifi (True) or not (False)"""
        return self._wlan.isconnected()

    def print_config(self):
        """print_config() - print config data on screen."""
        for key in self._config.keys():
            print('[{0}] = {1}'.format(key, self._config[key]))


    def change_access(self, user=None, passwrd=None):
        """change_access - change password for telnet and ftp access"""
        if (user == None) or (passwrd == None):
            print('WifiManager:: username and password must be specified')
            return

        server = Server() # from network
        # disable the server
        server.deinit()

        # enable the server again with new credentials
        # for example: remote access, ftp and telnet, not USB
        server.init(login=(user, passwrd), timeout=600)
        if USE_DEBUG:
            print('WifiManager::password is changed...')


    @property
    def __config(self):
        """returns config tuple"""
        return self._config

    @property
    def mac(self):
        """returns MAC-address of device"""
        mac = hexlify(self._wlan.mac(),':').decode() #pycom
        #return (mac) # lower case
        return mac.upper() #upper case


# test/usage
if __name__ == "__main__":
    import wifimanager
    wifi = wifimanager.WifiManager("wificonfig.json")
    params = wifi.connect()
    print('Device IP is {0}'.format(params[0])) # device IP
    wifi.print_config()
