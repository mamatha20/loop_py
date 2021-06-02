#perfect number is a positever divisisor that the sum of all positive divisors eg 6,28 is perfect number
num=int(input("enter the number"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(num,"it is perfect number")
else:
    print(num,"it is not perfect number")