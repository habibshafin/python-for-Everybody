fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0
for line in fh:
    sent = line.strip()
    st = sent.split()
    if len(st)==0:
        continue
    if st[0]=='From':
        print(st[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
