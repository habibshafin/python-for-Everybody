import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
import ssl
import json

#Don;t know about them as well
api_key = False
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

#Don't know why it does work without it
parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key


url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
counter = 0
for item in info["comments"] :
    counter = counter + int(item["count"])
print(counter)
