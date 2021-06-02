#    1
#   22
#  333
# 4444
# 55555
i=1
while i<=5:
    j=5
    while j>=i:
        print( " ",end=" ")
        j=j-1
    k=0
    while k<=j:
        print(i,end=" ")
        k=k+1
    i=i+1
    print()