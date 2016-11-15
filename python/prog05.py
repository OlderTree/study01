IList=[]
I=raw_input("please input a number:")
#IList.append(I)
while (I<>""):
	IList.append(int(I))
	I=raw_input("please input a number again(enter exit):")

print IList
IList.sort()
print IList

