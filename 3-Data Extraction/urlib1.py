# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum = 0
tags = soup('td')
for tag in tags :
    temp = str(tag.contents[0])
    if temp.startswith('<'):
        num = re.findall('([0-9]+)',temp)
        for n in num :
            number = int(n)
            sum = sum + number

print(sum)
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)
