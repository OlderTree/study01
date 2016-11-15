year=2300
year=input("input a year: ")
if year%100==0:
	if year%400==0:
		print year," is bissextile"
	else:
		print year," isnot bissextile"
elif year%4==0:
	print year," is bissextile"
else:
	print year," isnot bissextile"

