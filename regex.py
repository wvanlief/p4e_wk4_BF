import re

file = open(r'mbox.txt')
total = 0
cnt = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for n in numbers:
            cnt += 1
            total += int(n)

print(cnt, total)
