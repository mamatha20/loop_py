#write a program prime number 1 t0 100
i=1
while i<=100:
    j=1
    p=0
    while j<=i:
        if i%j==0:
            p=p+1
        j=j+1
    if p==2:
        print(i)
    i=i+1




