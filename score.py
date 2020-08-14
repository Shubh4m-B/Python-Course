score = input("Enter Score:")
s = float(score)
if s < 0.0 or s > 1.0 :
    print("Out of Range!")
    exit()
elif s>=0.9:
    grade = "A"
elif s>=0.8:
    grade = "B"
elif s>=0.7:
    grade = "C"
elif s>=0.6:
    grade = "D"
else:
    grade = "F"
print(grade) 