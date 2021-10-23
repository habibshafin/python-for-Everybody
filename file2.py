word = 'Banana'
word[0]='b'
print(word)


fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    quit()
count = 0.0
nos = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    str = line[19:len(line)]
    st = str.lstrip()
    num = float(st)
    count = count + num
    nos = nos + 1
print("Average spam confidence:",count/nos)
