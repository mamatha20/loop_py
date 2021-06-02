# check it is prime number or not
n=int(input("enter the number"))
i=2
while i<n:
    if n%i==0:
        print("it is not prime number")
        break
    i=i+1
else:
    print("it is prime number")
