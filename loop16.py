#If a number is divisible by the sum of its digits, then it will be known as a Harshad Number. For example:
#  The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).
#  Some Harshad numbers are 8, 54 156
num=int(input("enter the harshad number"))
i=num
sum=0
while i>0:
    b=i%10
    i=i//10
    sum=sum+b
if num%sum==0:
    print("it is harshad number")
else:
    print("it is not harshad number")