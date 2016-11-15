import math
l1=[]
l2=[]

def best_sqrt(x):
	y=0
	y=math.sqrt(x)
	if int(y)**2==x :
		#print y
		return True
	else:
		return False

for i in range(100000):
	if best_sqrt(i+100):
		l1.append(i)
	if best_sqrt(i+268):
		l2.append(i)

#print l1
#print l2
for n in l1:
	if n in l2:
		print n



