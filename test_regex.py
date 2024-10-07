import re

file = open(r'mbox.txt')
total = 0
cnt = 0
for line in file:
    if not line.startswith('From: '): continue
    line = line.split()
    print(line[1])
    orgs = re.findall('@(.+)', line[1])
    print(type(orgs[0]))

