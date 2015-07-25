from node import Node
from bst import Bst

class Avl(Bst):
	'''AVL Tree implementation. Values less than or equal to on the left,
	values greater than on the right. Always rebalances itself'''

	def add(self, data):

		'''Helper method for adding recursively'''
		def addNode(data, node):
			if node is None:
				self.size += 1
				return Node(data)
			elif data > node.getdata():
				node.setright(addNode(data, node.getright()))
				return node
			else:
				node.setleft(addNode(data, node.getleft()))
				return node

		self.root = addNode(data, self.root)

	def remove(self, data):
		'''For nodes with two children, the predecessor will be used as the replacement'''

		def two_children(data, parent, child):
			curr = child.getleft()
			prev = None
			while curr.getright():
				prev = curr
				curr = curr.getright()

			if (prev):
				prev.setright(None)

			replacement = curr
			replacement.setright(child.getright())
			replacement.setleft(child.getleft())

			if parent:
				if data > parent.getdata():
					parent.setright(replacement)

				else:
					parent.setleft(replacement)

			elif child is self.root:
				self.root = replacement


		def single_child(data, parent, child):
			replacement = child.getleft() if child.getleft() else child.getright()
			if parent:
				if data > parent.getdata():
					parent.setright(replacement)
				else:
					parent.setleft(replacement)

			elif child is self.root:
				self.root = replacement


		def no_child(data, parent, child):
			if parent is not None:
				if parent.getleft() is child:
					parent.setleft(None)
				else:
					parent.setright(None)

			elif child is self.root:
				self.root = None

		
		def helper_remove(data, parent, child):
			if child is None:
				return None
			elif data > child.getdata():
				helper_remove(data, child, child.getright())
			elif data < child.getdata():
				helper_remove(data, child, child.getleft())

			elif data == child.getdata():

				match = child.getdata()

				# Now we know we must remove it. Check the number of children
				num_children = 0
				num_children += 1 if child.getleft() else 0
				num_children += 1 if child.getright() else 0

				print 'num_children : ' + str(num_children)

				if num_children is 2:
					two_children(data, parent, child)

				elif num_children is 1:
					single_child(data, parent, child)

				else:
					no_child(data, parent, child)

				self.size -= 1
				return match

			else:
				return None

		return helper_remove(data, None, self.root)
