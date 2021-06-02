r=1
while r<=7:
	c=0
	while c<=7:
		if ((c==1 or c==6 or r==c ) and (c>0 and c<4) or (r==1 and c==5) or (r==2 and c==4) or c==5):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
#Patten M