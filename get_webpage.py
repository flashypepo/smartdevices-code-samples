# get webpage

import time
import socket

def http_get(url, port=80):
     _, _, host, path = url.split('/', 3)
     addr = socket.getaddrinfo(host, port)[0][-1]
     #print('addr=', addr)
     #s = socket.socket(socket.AF_INET, socket.SOCK_RAW) #ORG: socket.socket()
     s = socket.socket() # default: AF_INET, SOCK_STREAM, IPPROTO_TCP
     s.settimeout(10) #added 2018-0925, 60sec = 1 min
     s.connect(addr)
     s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))

     # TODO: response is read, but TIME_OUT
     #       is necessary to stop the while-loop
     #       Fix ??

     while True:
         data = s.read(200)
         if data:
             print(str(data, 'utf8'), end='')
         else:
             break

     s.close()

print (__name__ , ' loaded')
#print ('get_url(url_string) specified. Use it...')

if __name__ == '__main__':
    print('\nDEMO#1: getting test webpage...')
    http_get('http://micropython.org/ks/test.html', 80) #test page

    print('\n\nDEMO#2: getting the time...')
    http_get('http://time-a.nist.gov/', 13) # get the UTC-time

    print('\n\nDEMO#3: getting public IP...')
    http_get('http://ip.jsontest.com/', 80) # JSON file


# examples
# "towel.blinkenlights.nl", 23
# public IP
#http_get('http://miropython.org/ks/test.html')
