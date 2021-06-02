#write a program check prime number
num=int(input("enter the number"))
i=2
while i<num:
    if num%i==0:
        print("it is not prime number")
    i=i+1
else:
    print("it is prime number")