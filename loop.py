r=0
while r<5:
	c=0
	while c<=5:
		if ((c==1 or c==5 or r==c ) and  (c>0 and c<4 )  or (c==4)):
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
    #n