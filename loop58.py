c=0
while c<=4:
	r=0
	while r<=4:
		if r==0 or c==2 or c==0 or c==4:
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		r=r+1
	print()
	c=c+1
#E