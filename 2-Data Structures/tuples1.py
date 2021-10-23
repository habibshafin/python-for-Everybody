fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)

record = dict()
for line in fh:
    #sent = line.strip()
    #st = sent.split()
    st = line.strip().split()
    if len(st)==0:
        continue
    if st[0]=='From':
        time = st[5]
        t = time.split(':')
        hour = t[0]
        record[hour] = record.get(hour,0)+1

tmp = list()


tmp = [(k,v) for k,v in record.items()]
temp = sorted(tmp)
for (k,v) in temp:
    print(k,v)
