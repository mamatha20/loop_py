#an armstrong number is a number of 3 digit the sum of cubes of each digit is equal to the number ifself eg 153
num=int(input("enter tha armstrong number"))
i=num
sum=0
while i>0:
    b=i%10
    i=i//10
    sum=sum+b**3
if sum==num:
    print("it is armstrong number")
else:
    print("it is not armstrong number")