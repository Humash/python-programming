mark1=int(input("Enter mark1:"))
mark2=int(input("Enter mark2:"))
mark3=int(input("Enter mark3:"))
mark4=int(input("Enter mark4:"))
mark5=int(input("Enter mark5:"))
total=mark1+mark2+mark3+mark4+mark5
avg=total/5
if avg>90:
    print("The grade obtained is S")
elif avg>80 and avg<=90:
    print("The grade obtained is A")
elif avg>70 and avg<=80:
    print("The grade obtained is B")
elif avg>60 and avg<=70:
    print("The grade obtained is C")
elif avg>50 and avg<=60:
    print("The grade obtained is D")
else:
    print("Enter all the numbers as integers")
