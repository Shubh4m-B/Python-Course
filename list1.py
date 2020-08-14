fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    ls = line.split()
    for i in ls:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
