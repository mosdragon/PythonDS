from node import Node
from bst import Bst
import unittest

# CONSTANTS

# Data for root
ROOT_DATA = 10
# Data for left subtree
LEFT_DATA = 5
LL_DATA = 2
LR_DATA = 8
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

	def test_size(self):
		tree = Bst()
		self.assertEquals(tree.size, 0)
		self.assertEquals(tree.size, tree.getsize())

		# Set tree size to arbitrary number
		ARBITRARY_SIZE = 5
		tree.size = ARBITRARY_SIZE
		self.assertEquals(tree.size, ARBITRARY_SIZE)
		self.assertEquals(tree.size, tree.getsize())

		# Adding should increment size
		tree = balanced_tree()
		self.assertEquals(tree.getsize(), 7)
		FAR_RIGHT_DATA = 100
		tree.add(FAR_RIGHT_DATA)
		self.assertEquals(tree.getsize(), 8)


		# Removing should decrement size
		tree = balanced_tree()
		self.assertEquals(tree.getsize(), 7)
		tree.remove(ROOT_DATA)
		self.assertEquals(tree.getsize(), 6)

	def test_isempty(self):
		tree = Bst()
		self.assertTrue(tree.isempty())

		ARBITRARY_SIZE = 5
		tree.size = ARBITRARY_SIZE
		self.assertFalse(tree.isempty())

	def test_clear(self):
		tree = root_only()

		self.assertFalse(tree.isempty())
		self.assertEquals(tree.getsize(), 1)
		self.assertIsNotNone(tree.root)

		tree.clear()
		self.assertTrue(tree.isempty())
		self.assertEquals(tree.getsize(), 0)
		self.assertIsNone(tree.root)

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

		def remove_no_children():
			'''Removes a node that has no children. This node is not the root.'''
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


			def remove_no_children_root():
				'''Removing root of a tree with no children'''
				tree = root_only()
				self.assertIsNotNone(tree.root)
				self.assertEquals(tree.getsize(), 1)
				self.assertFalse(tree.isempty())
				self.assertEquals(tree.root, Node(ROOT_DATA))
				
				val = tree.remove(ROOT_DATA)

				self.assertEquals(tree.getsize(), 0)
				self.assertTrue(tree.isempty())
				self.assertEquals(val, ROOT_DATA)
				self.assertIsNone(tree.root)

			remove_no_children_root()


		def remove_one_child():
			'''Removing node that has one child'''
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

		
			def remove_one_child_root():
				'''Removing root in a tree where the root has only one child'''
				tree = Bst()
				tree.add(ROOT_DATA)
				tree.add(LEFT_DATA)
				self.assertFalse(tree.isempty())
				self.assertEquals(tree.getsize(), 2)
				self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)

				val = tree.remove(ROOT_DATA)
				
				self.assertFalse(tree.isempty())
				self.assertEquals(tree.getsize(), 1)
				self.assertEquals(val, ROOT_DATA)
				self.assertIsNotNone(tree.root)
				self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
				self.assertEquals(tree.root, Node(LEFT_DATA))

			remove_one_child_root()


		def remove_two_children():
			'''Removes node with two children, using predecessor as replacement'''

			def has_no_right_subtree():
				'''Predecessor is to the immediate left of removed node'''
				tree = balanced_tree()

				self.assertEquals(tree.getsize(), 7)

				tree.remove(LEFT_DATA)

				self.assertEquals(tree.getsize(), 6)
				left_replacement = tree.root.getleft()
				self.assertEquals(left_replacement.getdata(), LL_DATA)
				self.assertEquals(left_replacement.getheight(), 1)
				self.assertEquals(left_replacement.getright().getdata(), LR_DATA)
				self.assertIsNone(left_replacement.getleft())

			def has_right_subtree():
				'''Predecessor is one left, then all the way down right of removed node'''
				# great-grandchild and great-great-grandchild, left side
				GG_CHILD_DATA = 3
				GGG_CHILD_DATA = 4

				tree = balanced_tree()
				self.assertEquals(tree.getsize(), 7)
				
				tree.add(GG_CHILD_DATA)
				tree.add(GGG_CHILD_DATA)

				self.assertEquals(tree.getsize(), 9)
				gg_child_node = tree.root.getleft().getleft().getright()
				self.assertIsNotNone(gg_child_node)
				ggg_child_node = gg_child_node.getright()
				self.assertIsNotNone(ggg_child_node)

				self.assertEquals(gg_child_node.getdata(), GG_CHILD_DATA)
				self.assertEquals(ggg_child_node.getdata(), GGG_CHILD_DATA)


				val = tree.remove(LEFT_DATA)

				self.assertEquals(tree.getsize(), 8)
				self.assertEquals(val, LEFT_DATA)

				left_node = tree.root.getleft()
				self.assertIsNotNone(left_node)
				self.assertEquals(left_node.getdata(), GGG_CHILD_DATA)

				self.assertIsNotNone(left_node.getright())
				self.assertEquals(left_node.getright().getdata(), LR_DATA)

				self.assertIsNotNone(left_node.getleft())
				self.assertEquals(left_node.getleft().getdata(), LL_DATA)

				self.assertIsNotNone(left_node.getleft().getright())
				self.assertEquals(left_node.getleft().getright().getdata(), GG_CHILD_DATA)
				
			def remove_two_children_root():
				'''Removes root of a tree that has two children for the root'''
				tree = balanced_tree()

				self.assertEquals(tree.getsize(), 7)
				self.assertEquals(tree.root.getdata(), ROOT_DATA)

				val = tree.remove(ROOT_DATA)

				self.assertEquals(tree.getsize(), 6)
				self.assertEquals(val, ROOT_DATA)

				self.assertIsNotNone(tree.root)
				self.assertEquals(tree.root.getdata(), LR_DATA)

				root = tree.root

				# Left subtree should be changed. LR_DATA is now in the root,
				# So the LR node will be None
				left_node = root.getleft()
				self.assertIsNotNone(left_node)
				self.assertEquals(left_node.getdata(), LEFT_DATA)

				self.assertIsNotNone(left_node.getleft())
				self.assertEquals(left_node.getleft().getdata(), LL_DATA)
				self.assertIsNone(left_node.getright())


				# Right subtree should be unchanged
				right_node = root.getright()
				self.assertIsNotNone(right_node)
				self.assertEquals(right_node.getdata(), RIGHT_DATA)

				self.assertIsNotNone(right_node.getleft())
				self.assertEquals(right_node.getleft().getdata(), RL_DATA)
				self.assertIsNotNone(right_node.getright())
				self.assertEquals(right_node.getright().getdata(), RR_DATA)

			has_no_right_subtree()
			has_right_subtree()
			remove_two_children_root()


		remove_no_children()
		remove_one_child()
		remove_two_children()

	def test_contains(self):
		# Test with a root only
		tree = root_only()

		self.assertFalse(tree.isempty())
		self.assertEquals(tree.getsize(), 1)
		self.assertIsNotNone(tree.root)
		self.assertEquals(tree.root.getdata(), ROOT_DATA)

		# Should contain the root data
		self.assertTrue(tree.contains(ROOT_DATA))
		
		# Should not contain any of the children data
		self.assertFalse(tree.contains(LEFT_DATA))
		self.assertFalse(tree.contains(RIGHT_DATA))

		# Should not contain any of the grandchildren data
		self.assertFalse(tree.contains(LL_DATA))
		self.assertFalse(tree.contains(LR_DATA))
		self.assertFalse(tree.contains(RL_DATA))
		self.assertFalse(tree.contains(RR_DATA))

		tree.remove(ROOT_DATA)
		self.assertTrue(tree.isempty())
		self.assertIsNone(tree.root)
		self.assertFalse(tree.contains(ROOT_DATA))


		# Now test with the balanced tree
		tree = balanced_tree()

		self.assertFalse(tree.isempty())
		self.assertEquals(tree.getsize(), 7)
		self.assertIsNotNone(tree.root)
		self.assertEquals(tree.root.getdata(), ROOT_DATA)

		# Should contain the root data
		self.assertTrue(tree.contains(ROOT_DATA))
		
		# Should not contain any of the children data
		self.assertTrue(tree.contains(LEFT_DATA))
		self.assertTrue(tree.contains(RIGHT_DATA))

		# Should not contain any of the grandchildren data
		self.assertTrue(tree.contains(LL_DATA))
		self.assertTrue(tree.contains(LR_DATA))
		self.assertTrue(tree.contains(RL_DATA))
		self.assertTrue(tree.contains(RR_DATA))

		TO_ADD_DATA = 50

		self.assertFalse(tree.contains(TO_ADD_DATA))
		tree.add(TO_ADD_DATA)
		self.assertTrue(tree.getsize(), 8)
		self.assertTrue(tree.contains(TO_ADD_DATA))

		# Finally, test with an empty tree
		tree = Bst()

		self.assertTrue(tree.isempty())
		self.assertIsNone(tree.root)

		# Should not contain the root data
		self.assertFalse(tree.contains(ROOT_DATA))
		
		# Should not contain any of the children data
		self.assertFalse(tree.contains(LEFT_DATA))
		self.assertFalse(tree.contains(RIGHT_DATA))

		# Should not contain any of the grandchildren data
		self.assertFalse(tree.contains(LL_DATA))
		self.assertFalse(tree.contains(LR_DATA))
		self.assertFalse(tree.contains(RL_DATA))
		self.assertFalse(tree.contains(RR_DATA))

	def test_inorder(self):
		pass

	def test_preorder(self):
		pass

	def test_postorder(self):
		pass

	def test_levelorder(self):
		pass

unittest.main()

