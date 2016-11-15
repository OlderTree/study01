year=input("input a year:")
month=input("input a month:")
day=input("input a day:")

def bissextile(year):
	if year % 100 ==0 :
		if year % 400 ==0 :
			return True
		else:
			return False
	else:
		if year % 4 ==0 :
			return True
		else:
			return False
monthtup=(31,28,31,30,31,30,31,31,30,31,30,31)

if bissextile(year) and month >2 :
	allday=1+day
	for dn in monthtup[0:month-1:1]:
		allday=allday + dn
else:
	allday=0+day
	for dn in monthtup[0:month-1:1]:
		allday=allday +dn

print "Days:",allday

