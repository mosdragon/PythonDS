
class Node:
	'''This is a node class that can hold a left child and a right child'''

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		self.height = 0


	def determineheight(self):
		if (self.left):
			left_height = self.left.getheight()
			if left_height + 1 > self.getheight():
				self.height = left_height + 1

		if (self.right):
			right_height = self.right.getheight()
			if right_height + 1 > self.getheight():
				self.height = right_height + 1

		if (not (self.right and self.left)):
			self.height = 0

	def setleft(self, left):
		self.left = left
		self.determineheight()


	def getleft(self):
		return self.left

	def setright(self, right):
		self.right = right
		self.determineheight()

	def getright(self):
		return self.right

	def getheight(self):
		return self.height

	def setdata(self, data):
		self.data = data

	def getdata(self):
		return self.data