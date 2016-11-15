cl=[100000,200000,400000,600000,1000000]
clreverse=[x for x in cl[::-1]]
clp=[0.1,0.07,0.05,0.03,0.015,0.01]
clv=[10000,17000,27000,33000,39000]
lr=input("please input a number: ")
if lr<>0 :
	lrnum=lr
	for i,j in enumerate(clreverse):
		if lrnum >= j :
			more=lrnum-j
			classid=4-i
			break
jj=clv[classid] + more * clp[classid+1]
print more
print "Bonus class:", classid
print "Your Bonus:", jj

		
