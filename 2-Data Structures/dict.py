fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

record = dict()
for line in fh:
    sent = line.strip()
    st = sent.split()
    if len(st)==0:
        continue
    if st[0]=='From':
        record[st[1]] = record.get(st[1],0)+1

maxName = None
maxTimes = None
for name,times in record.items():
    if maxTimes is None or maxTimes < times:
        maxTimes = times
        maxName = name
print(maxName,maxTimes)
