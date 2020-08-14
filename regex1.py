import re

fname = input("Enter file name:")
if len(fname) < 1:
    fname = "regex_sum.txt"
sum = 0
fhandle = open(fname)
for line in fhandle:
    x = re.findall("[0-9]+", line)
    for i in x:
        y = int(i)
        sum = sum + y
print("Sum:", sum)
