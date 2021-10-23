fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    quit()

lst = list()
for line in fh:
    l = line.rstrip()
    sent = l.split()
    for i in range(len(sent)):
        if sent[i] in lst:
            continue
        lst.append(sent[i])

print(lst)
