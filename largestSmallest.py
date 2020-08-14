largest = None
smallest = None
cont = True

while cont == True:
    num = input("Enter a number:")
    if num == "done":
        cont = False
        break
    try:
        fnum = float(num)
    except:
        print("Invalid Input")
        continue
    if largest is None or fnum > largest:
        largest = fnum
    if smallest is None or fnum < smallest:
        smallest = fnum

print("Maximum ",largest)
print("Minimum ",smallest)

    
