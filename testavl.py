from avl import Avl

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



tree = Avl()
assert tree.getsize() is 0
assert tree.isempty()
assert tree.inorder() == []

tree.add(10)
assert tree.getsize() is 1
assert not tree.isempty()
assert tree.inorder() == [10]

print "REMOVE NO CHILDREN"
tree.remove(10)
assert tree.getsize() is 0
assert tree.isempty()
assert tree.inorder() == []


tree.add(10)
tree.add(5)
tree.add(20)
assert tree.getsize() is 3
assert not tree.isempty()
assert tree.inorder() == [5, 10, 20]
assert tree.preorder() == [10, 5, 20]
assert tree.postorder() == [5, 20, 10]

tree.add(6)
tree.add(4)

tree.add(15)
tree.add(25)

print "REMOVE TWO CHILDREN"
tree.remove(10)

print "CLEAR"

tree_print(tree)

tree.clear()
tree.add(10)
tree.add(5)
tree.add(20)
tree.add(4)
tree.add(6)
tree.add(15)
tree.add(25)

tree.add(7)
tree.add(3)
assert tree.getsize() ==  len(tree.inorder())

tree_print(tree)

print "REMOVE NO CHILD : 7"
tree.remove(7)
assert tree.getsize() == len(tree.inorder())


tree_print(tree)


tree.add(7)
tree.add(8)

print
tree_print(tree)
print tree.levelorder()
print
print "REMOVE ONE CHILD : 7"
tree.remove(7)
print
tree_print(tree)
print tree.levelorder()


print

tree.add(7)
tree.add(9)
tree_print(tree)



