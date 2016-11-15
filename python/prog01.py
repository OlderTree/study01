xl=(1,2,3,4)
yl=range(3)
yls=""
yll=[]

for i in xl:
	for j in xl:
		for k in xl:
			if (i<>j and j<>k and i<>k):	
				#yl[0]=str(i)
				#yl[1]=str(j)
				#yl[2]=str(k)
				yls=str(i) + str(j) + str(k)
				print yls
				yll.append(yls)
				
				


print yll
print len(yll)
