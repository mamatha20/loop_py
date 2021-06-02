#factorial number
num=int(input("enter the number"))
fac=1
if num==0:
    print(1)
else:
    while num>=1:
        fac=fac*num
        num=num-1
    print(fac)