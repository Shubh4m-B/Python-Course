name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if line.startswith("From "):
        li1 = line.split()
        li2 = li1[5].split(":")
        count[li2[0]] = count.get(li2[0],0) + 1

lis = list()

for k,v in count.items():
    lis.append((k,v))

for tup in sorted(lis):
    print(tup[0],tup[1])


