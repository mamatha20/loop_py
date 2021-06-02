n=int(input("Enter number:"))
a=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(a==rev):
    print(" it is a palindrome!")
else:
    print("it not a palindrome!")
# check it is palindrome no. Or not