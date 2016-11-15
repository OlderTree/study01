# 9*9 multiplication list
i=1
j=1
line=""
for i in range(10):
#	line=""
	for j in range(10):
		if i==0 or j==0 :
			continue
		if i==j:
			line=line +  "%d*%d=%-4d\n" %(i,j,i*j)
			break
		else:
			line=line + "%d*%d=%-4d" %(i,j,i*j)
print line
