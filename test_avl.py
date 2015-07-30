from avl import Avl
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
    tree = Avl()
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
    tree = Avl()
    # Add root
    tree.add(ROOT_DATA)

    # Add left child
    tree.add(LEFT_DATA)

    # Add left's child
    tree.add(LL_DATA)

    return tree


def root_only():
    tree = Avl()
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


class AvlTester(unittest.TestCase):

    def test_add(self):
        # Left Left case
        # tree = Avl()
        # tree.add(ROOT_DATA)
        # self.assertEquals(tree.root.getdata(), ROOT_DATA)
        # tree.add(LEFT_DATA)
        # self.assertEquals(tree.root.getdata(), ROOT_DATA)
        # tree.add(RIGHT_DATA)
        # self.assertEquals(tree.root.getdata(), ROOT_DATA)
        # tree.add(LL_DATA)
        # self.assertEquals(tree.root.getdata(), ROOT_DATA)
        #
        # tree.add(0)
        # self.assertNotEquals(tree.root.getleft().getdata(), LEFT_DATA)
        # self.assertEquals(tree.root.getleft().getdata(), LL_DATA)

        tree = Avl()
        tree.add(ROOT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        tree.add(LEFT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        tree.add(LL_DATA)
        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getdata(), LEFT_DATA)

