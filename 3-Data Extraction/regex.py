import re
fhandle = open('sample.txt')
sum = 0
for line in fhandle:
    if line.startswith('\n'):
        continue
    str = line.strip()
    #print(str)
    temp = re.findall('[0-9]+',str)
    for num in temp:
        number = int(num)
        sum = sum + number

print(sum)
