i=1
while i<=5:
    j=5
    while j>=i:
        print(" ",end=" ")
        j=j-1
    k=1
    while k<=i:
        print(chr(k+64),end=" ")
        k=k+1
    i=i+1
    print()