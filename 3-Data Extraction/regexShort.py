import re
fhandle = open('sample.txt')
print(sum(int (i)for i in re.findall('[0-9]+',fhandle.read())))
