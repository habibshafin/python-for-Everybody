fname = input("Enter file name:")
try :
    fh = open(fname)
except :
    quit()

str = fh.read()
print(str.upper())
