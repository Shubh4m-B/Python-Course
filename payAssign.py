hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour:")
r = float(rate)
if h > 40:
    pay1 = h*r
    pay2 = (h-40)*r*0.5
    pay1 = pay2 + pay1
else:
    pay1 = h*r
print(pay1)