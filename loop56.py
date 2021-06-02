r= 0
while r<=5:
	c= 0
	while c<=4:
		if (c==2 or r==0):
			print('*',end=' ')
		else:
			print(' ',end= ' ')
		c= c+1
	print()
	r= r+1
# pattern T