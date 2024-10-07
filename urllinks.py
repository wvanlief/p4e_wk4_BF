import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Dione.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
url_new = str()
url_to = str()
i=0
j=0
pos = 18
repeat = 7
#for tag in tags:
#    print(tag.get('href', None))
while i < repeat:
    url_new = tags[pos-1].get('href', None)
    print(url_new)
    html = urllib.request.urlopen(url_new, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i += 1