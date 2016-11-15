def line_conf():
	b=25
	def line(x):
		return 2*x+b
	return line

b=50
my_line=line_conf()
print(my_line(10))

