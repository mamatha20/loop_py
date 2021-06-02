#So the happy number is a number, where starting with any positive integers replace the number by the sum of squares of
#  its digits, this process will be repeated until it becomes 1, otherwise it will loop endlessly in a cycle. 
# Those numbers, when the 1 has found,
#  they will be happy number.
n=int(input("enter the number"))
sum=0
i=1
while n>0:
	i=n%10
	sum=sum+(i*i)
	n=n//10
	while i!=1 and i!=4:
		i=i+1
	if i==1:
		print("hn")
	else:
		print(" not hn")
    
n=int(input("enter the number"))
sum=0
i=1
while n>0:
	i=n%10
	sum=sum+(i*i)
	n=n//10
	while i!=1 and i!=4:
		i=i+1
if i==1:
	print("hn")
else:
    print("it is not hp")