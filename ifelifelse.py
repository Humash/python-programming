mark=int(input("Enter the marks obtained by a student:"))
if mark>90:
    print("The grade obtained is S")
elif mark>80 and mark<=90:
    print("The grade obtained is A")
elif mark>70 and mark<=80:
    print("The grade obtained is B")
elif mark>60 and mark<=70:
    print("The grade obtained is C")
elif mark>50 and mark<=60:
    print("The grade obtained is D")
else:
    print("Enter all the numbers as integers")
