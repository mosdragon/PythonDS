from node import Node
from bst import Bst
import unittest
# CONSTANTS

# Data for root
ROOT_DATA = 10
# Data for left subtree
LEFT_DATA = 5
LL_DATA = 4
LR_DATA = 6
# Data for right subtree
RIGHT_DATA = 20
RL_DATA = 15
RR_DATA = 25

def balanced_tree():
	tree = Bst()
	# Add root
	tree.add(ROOT_DATA)

	# Add children
	tree.add(LEFT_DATA)
	tree.add(RIGHT_DATA)

	# Add left's children
	tree.add(LL_DATA)
	tree.add(LR_DATA)

	# Add right's children
	tree.add(RL_DATA)
	tree.add(RR_DATA)

	return tree

def left_chain_tree():
	tree = Bst()
	# Add root
	tree.add(ROOT_DATA)

	# Add left child
	tree.add(LEFT_DATA)

	# Add left's child
	tree.add(LL_DATA)

	return tree

def root_only():
	tree = Bst()
	tree.add(ROOT_DATA)
	return tree

def tree_print(tree):
	power = 0
	threshold = 2 ** power
	size = tree.getsize()

	count = 0

	text = ""
	for index, val in enumerate(tree.levelorder()):
		text += str(val) + " "
		count += 1
		if count == threshold or index + 1 is size:

			print text
			text = ""
			power += 1
			threshold = 2 ** power
			count = 0

class BstTester(unittest.TestCase):

	def test_init(self):
		tree = Bst()
		self.assertEquals(tree.size, 0)
		self.assertIsNone(tree.root)

	def test_getsize(self):
		tree = Bst()
		self.assertEquals(tree.size, 0)
		self.assertEquals(tree.size, tree.getsize())

		# Set tree size to arbitrary number
		UPDATED_SIZE = 5
		tree.size = UPDATED_SIZE
		self.assertEquals(tree.size, UPDATED_SIZE)
		self.assertEquals(tree.size, tree.getsize())

	def test_add(self):
		tree = Bst()
		tree.add(ROOT_DATA)

		self.assertEquals(tree.getsize(), 1)
		self.assertIsNotNone(tree.root)
		self.assertEquals(tree.root.getheight(), 0)
		self.assertEquals(tree.root.getdata(), ROOT_DATA)

		# Add left child
		tree.add(LEFT_DATA)
		self.assertEquals(tree.getsize(), 2)
		self.assertIsNotNone(tree.root.getleft())
		self.assertIsNone(tree.root.getright())
		self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
		self.assertEquals(tree.root.getheight(), 1)

		# Add right child
		tree.add(RIGHT_DATA)
		self.assertEquals(tree.getsize(), 3)
		self.assertIsNotNone(tree.root.getleft())
		self.assertIsNotNone(tree.root.getright())
		self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)
		self.assertEquals(tree.root.getheight(), 1)

		# Add granchildren to left child
		tree.add(LL_DATA)
		self.assertEquals(tree.getsize(), 4)
		self.assertIsNotNone(tree.root.getleft().getleft())
		self.assertIsNone(tree.root.getleft().getright())
		self.assertEquals(tree.root.getleft().getleft().getdata(), LL_DATA)
		self.assertEquals(tree.root.getheight(), 2)
		self.assertEquals(tree.root.getleft().getheight(), 1)

		tree.add(LR_DATA)
		self.assertEquals(tree.getsize(), 5)
		self.assertIsNotNone(tree.root.getleft().getleft())
		self.assertIsNotNone(tree.root.getleft().getright())
		self.assertEquals(tree.root.getleft().getright().getdata(), LR_DATA)
		self.assertEquals(tree.root.getheight(), 2)
		self.assertEquals(tree.root.getleft().getheight(), 1)

		# Add grandchildren to right child
		tree.add(RL_DATA)
		self.assertEquals(tree.getsize(), 6)
		self.assertIsNotNone(tree.root.getright().getleft())
		self.assertIsNone(tree.root.getright().getright())
		self.assertEquals(tree.root.getright().getleft().getdata(), RL_DATA)
		self.assertEquals(tree.root.getheight(), 2)
		self.assertEquals(tree.root.getright().getheight(), 1)

		tree.add(RR_DATA)
		self.assertEquals(tree.getsize(), 7)
		self.assertIsNotNone(tree.root.getright().getleft())
		self.assertIsNotNone(tree.root.getright().getright())
		self.assertEquals(tree.root.getright().getright().getdata(), RR_DATA)
		self.assertEquals(tree.root.getheight(), 2)
		self.assertEquals(tree.root.getright().getheight(), 1)

	def test_remove(self):

		# Removing Node w/ no children
		tree = balanced_tree()
		self.assertEquals(tree.getsize(), 7)
		val = tree.remove(LL_DATA)
		self.assertEquals(tree.getsize(), 6)
		self.assertEquals(val, LL_DATA)

		# Only LL child should be None. Rest should have same expected values
		self.assertEquals(tree.root.getdata(), ROOT_DATA)

		self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
		self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)

		self.assertIsNone(tree.root.getleft().getleft())
		self.assertEquals(tree.root.getleft().getright().getdata(), LR_DATA)
		self.assertEquals(tree.root.getright().getleft().getdata(), RL_DATA)
		self.assertEquals(tree.root.getright().getright().getdata(), RR_DATA)

		# Removing Root w/ no children
		tree = root_only()
		self.assertEquals(tree.getsize(), 1)
		self.assertEquals(tree.root, Node(ROOT_DATA))



		# Removing Node w/ one child
		tree = left_chain_tree()
		self.assertEquals(tree.getsize(), 3)
		val = tree.remove(LL_DATA)
		self.assertEquals(tree.getsize(), 2)
		self.assertEquals(val, LL_DATA)


		# Only left child and root have values. Rest should be None
		self.assertEquals(tree.root.getdata(), ROOT_DATA)
		self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)

		self.assertIsNone(tree.root.getright())
		self.assertIsNone(tree.root.getleft().getleft())
		self.assertIsNone(tree.root.getleft().getright())


unittest.main()



# tree = Bst()
# assert tree.getsize() is 0
# assert tree.isempty()
# assert tree.inorder() == []

# tree.add(10)
# assert tree.getsize() is 1
# assert not tree.isempty()
# assert tree.inorder() == [10]

# print "REMOVE NO CHILDREN"
# tree.remove(10)
# assert tree.getsize() is 0
# assert tree.isempty()
# assert tree.inorder() == []


# tree.add(10)
# tree.add(5)
# tree.add(20)
# assert tree.getsize() is 3
# assert not tree.isempty()
# assert tree.inorder() == [5, 10, 20]
# assert tree.preorder() == [10, 5, 20]
# assert tree.postorder() == [5, 20, 10]

# tree.add(6)
# tree.add(4)

# tree.add(15)
# tree.add(25)

# print "REMOVE TWO CHILDREN"
# tree.remove(10)

# print "CLEAR"

# tree_print(tree)

# tree.clear()
# tree.add(10)
# tree.add(5)
# tree.add(20)
# tree.add(4)
# tree.add(6)
# tree.add(15)
# tree.add(25)

# tree.add(7)
# tree.add(3)
# assert tree.getsize() ==  len(tree.inorder())

# tree_print(tree)

# print "REMOVE NO CHILD : 7"
# tree.remove(7)
# assert tree.getsize() == len(tree.inorder())


# tree_print(tree)


# tree.add(7)
# tree.add(8)

# print
# tree_print(tree)
# print tree.levelorder()
# print
# print "REMOVE ONE CHILD : 7"
# tree.remove(7)
# print
# tree_print(tree)
# print tree.levelorder()


# print

# tree.add(7)
# tree.add(9)
# tree_print(tree)



