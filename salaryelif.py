salary=float(input("Enter the salary of the Employee:"))
if salary==10000:
    print("The bonus amount to be credited is",10000*0.5)
elif salary>10000:
    print("The bonus amount to be credited is",10000*0.075)
elif salary<=2000:
        expereince=int(input("Enter expereince:"))
        if expereince>5:
            print("The bonus amount to be credited is",salary*0.2)
        elif expereince<=5:
            print("The bonus amount to be credited is",salary*0.1)
else:
    print("Invalid number")
