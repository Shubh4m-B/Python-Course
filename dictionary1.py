name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
li = list()
count = dict()
for line in handle:
    if line.startswith('From '):
        li = line.split()
        count[li[1]] = count.get(li[1],0) + 1

# print(count)

maxcount = 0
for i,j in count.items():
    if j > maxcount:
        maxcount = j
        maxperson = i

print(maxperson,maxcount)
            