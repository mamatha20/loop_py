r=0
while r<=5:
	c=0
	while c<=6:
		if ((c==0 or c==4 and r!=0) or (r==0 or r==3) and (c>0 and c<4)):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
#Output A