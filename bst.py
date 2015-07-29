from node import Node

'''Binary Search Tree implementation. Values less than on the left,
values greater than on the right. No duplicate data entries allowed'''
class Bst:

	def __init__(self):
		self.root = None
		self.size = 0

	def getsize(self):
		return self.size

	def isempty(self):
		return (self.size is 0)

	def add(self, data):

		'''Helper method for adding recursively'''
		def helper_add(data, node):
			if node is None:
				self.size += 1
				return Node(data)
			elif data > node.getdata():
				node.setright(helper_add(data, node.getright()))
				node.determineheight()
				return node
			elif data < node.getdata():
				node.setleft(helper_add(data, node.getleft()))
				node.determineheight()
				return node
			else:
				return node

		self.root = helper_add(data, self.root)


	def contains(self, data):

		def helper_contains(data, node):
			if node is None:
				return False
			
			elif data > node.getdata():
				return helper_contains(data, node.getright())
			
			elif data < node.getdata():
				return helper_contains(data, node.getleft())
			
			elif data == node.getdata():
				return True

			else:
				return False


		return helper_contains(data, self.root)


	def remove(self, data):

		def two_children(data, parent, child):
			'''For nodes with two children, the predecessor will be used as the replacement'''
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
				result = helper_remove(data, child, child.getright())
				child.determineheight()
				return result
			
			elif data < child.getdata():
				result = helper_remove(data, child, child.getleft())
				child.determineheight()
				return result

			elif data == child.getdata():

				result = child.getdata()

				# Now we know we must remove it. Check the number of children
				num_children = 0
				num_children += 1 if child.getleft() else 0
				num_children += 1 if child.getright() else 0

				if num_children is 2:
					two_children(data, parent, child)

				elif num_children is 1:
					single_child(data, parent, child)

				else:
					no_child(data, parent, child)

				self.size -= 1
				return result

			else:
				return None

		return helper_remove(data, None, self.root)


	# def getroot(self):
	# 	return self.root

	def inorder(self):
		result = []

		'''Helper method for in-order traversal of BST'''
		def inorderhelper(node):
			if node is None:
				pass
			else:
				inorderhelper(node.getleft())
				result.append(node.getdata())
				inorderhelper(node.getright())

		inorderhelper(self.root)
		return result

	def preorder(self):
		result = []

		'''Helper method for pre-order traversal of BST'''
		def preorderhelper(node):
			if node is None:
				pass
			else:
				result.append(node.getdata())
				preorderhelper(node.getleft())
				preorderhelper(node.getright())

		preorderhelper(self.root)
		return result

	def postorder(self):
		result = []

		'''Helper method for post-order traversal of BST'''
		def postorderhelper(node):
			if node is None:
				pass
			else:
				postorderhelper(node.getleft())
				postorderhelper(node.getright())
				result.append(node.getdata())

		postorderhelper(self.root)
		return result

	def levelorder(self):
		results = []
		queue = [self.root]
		size = 1
		index = 0
		while index < size:
			curr = queue[index]
			if curr:
				results.append(curr.getdata())
				queue.append(curr.getleft())
				queue.append(curr.getright())
				size += 2
			index += 1

		return results

	def clear(self):
		self.size = 0
		self.root = None
