# 1
# 22
# 333
# 4444
# 55555
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    i=i+1
    print()

#second method
i=1
while i<=5:
    print(str(i)*i)
    i=i+1
