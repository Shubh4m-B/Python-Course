# Use word.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    ly = line.rstrip()
    lx = ly.upper()
    print(lx)
