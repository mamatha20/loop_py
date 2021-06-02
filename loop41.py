i=1
while i<=4:
    j=1
    while j<=4:
        if (j==1 or j==4) or (i==1 or i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()