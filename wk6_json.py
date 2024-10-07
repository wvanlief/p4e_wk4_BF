import json
import urllib.error
import urllib.request

#url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_2007685.json"

uh = urllib.request.urlopen(url)

data = uh.read()
info = json.loads(data)
print('User count:', len(info))


#print(info['comments'])
total = 0
cmts = 0
for comment in info['comments']:
    cmts += 1
    total += comment['count']

print(cmts, total)
