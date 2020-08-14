# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        count = count + 1
        ls = line.strip()
        index = ls.find(":") + 1
        num = float(ls[index:])
        s = s + num
avg = s/count
avg = round(avg, 15)
print(avg)

