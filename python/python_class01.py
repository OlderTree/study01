class human(object):
	def __init__(self,ig):
		self.gender=ig
	def printgd(self):
		print self.gender

ll=human("male")
print ll.gender
ll.printgd()

