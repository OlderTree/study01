newrbt=1
growning=0
adult=0
month=24	
print 1,"month:",newrbt,growning,adult,newrbt+growning+adult
for m in range(month):
	new=newrbt
	adult=adult+growning
	newrbt=adult
	growning=new
	print m+2,"month:",newrbt,growning,adult,newrbt+growning+adult

