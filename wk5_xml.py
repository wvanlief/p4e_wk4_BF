import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_2007684.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')
total = 0
for item in range (0, len(results)):
    #print(results[item].text)
    total += int(results[item].text)
print(len(results))
print(total)