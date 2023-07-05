b=int(input("enter the number"))
e=[]
o=[]
for a in range(1,b+1):
    if a%2==0:
        e.append(a)
    else:
        o.append(a)
print(b)
print("odd number=",o)
print("even number=",e)
