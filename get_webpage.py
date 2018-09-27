# get webpages via HTTP requests-response
# required: lib/urequests
# 2018-0927 Peter  - College 4 samples.

import urequests as requests

print('\nDEMO#1: getting test webpage...')
r = requests.get('http://micropython.org/ks/test.html')
#print(r)
print(r.content)
#print(r.text)

print('\n\nDEMO#3: getting public IP...')
# zie opdracht 5 - maak dat zelf op basis van demo#1 voorbeeld.
