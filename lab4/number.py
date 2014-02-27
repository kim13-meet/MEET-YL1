class Integer(object):
	def __init__(self, number):
		self.number = number

	def __Display__(self):
		print self.number

if __name__ == "__main__":
	x = Integer(8)
	x.__Display__()
	y = Integer(5)
	x.__Display__()