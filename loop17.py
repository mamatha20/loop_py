# the sum of the factorial of each of the digits of the number equals the given number, 
# then such a number is called a strong number. 
# Example is 145 as 1!
num=int(input("enter the  strong number"))
a=num
sum=0
while num>0:
    i=1
    f=1
    b=num%10
    while i<=b:
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if a==sum:
    print("it is strong number")
else:
    print("it is not strong number")

