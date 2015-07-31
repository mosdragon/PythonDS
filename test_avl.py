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

    def test_add_left_left_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(LEFT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(LL_DATA)
        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)

        self.assertEquals(tree.root.getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LL_DATA)
        self.assertEquals(tree.root.getright().getdata(), ROOT_DATA)

    def test_add_left_right_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(LEFT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(LR_DATA)
        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)

        self.assertEquals(tree.root.getdata(), LR_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), ROOT_DATA)

    def test_add_right_right_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(RIGHT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(RR_DATA)
        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)

        self.assertEquals(tree.root.getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RR_DATA)

    def test_add_right_left_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(RIGHT_DATA)
        self.assertEquals(tree.root.getdata(), ROOT_DATA)

        tree.add(RL_DATA)
        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)

        self.assertEquals(tree.root.getdata(), RL_DATA)
        self.assertEquals(tree.root.getleft().getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)

    def test_remove_left_left_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        tree.add(LEFT_DATA)
        tree.add(RIGHT_DATA)
        tree.add(LL_DATA)

        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getleft().getleft().getdata(), LL_DATA)
        self.assertEquals(tree.getsize(), 4)

        val = tree.remove(RIGHT_DATA)

        self.assertEquals(val, RIGHT_DATA)
        self.assertEquals(tree.getsize(), 3)

        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LL_DATA)
        self.assertEquals(tree.root.getright().getdata(), ROOT_DATA)

    def test_remove_left_right_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        tree.add(LEFT_DATA)
        tree.add(RIGHT_DATA)
        tree.add(LR_DATA)

        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getleft().getright().getdata(), LR_DATA)
        self.assertEquals(tree.getsize(), 4)

        val = tree.remove(RIGHT_DATA)
        self.assertEquals(val, RIGHT_DATA)
        self.assertEquals(tree.getsize(), 3)

        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getdata(), LR_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), ROOT_DATA)

    def test_remove_right_right_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        tree.add(LEFT_DATA)
        tree.add(RIGHT_DATA)
        tree.add(RR_DATA)

        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getright().getright().getdata(), RR_DATA)
        self.assertEquals(tree.getsize(), 4)

        val = tree.remove(LEFT_DATA)

        self.assertEquals(val, LEFT_DATA)
        self.assertEquals(tree.getsize(), 3)

        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RR_DATA)

    def test_remove_right_left_case(self):
        tree = Avl()

        tree.add(ROOT_DATA)
        tree.add(LEFT_DATA)
        tree.add(RIGHT_DATA)
        tree.add(RL_DATA)

        self.assertEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getleft().getdata(), LEFT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)
        self.assertEquals(tree.root.getright().getleft().getdata(), RL_DATA)
        self.assertEquals(tree.getsize(), 4)

        val = tree.remove(LEFT_DATA)
        self.assertEquals(val, LEFT_DATA)
        self.assertEquals(tree.getsize(), 3)

        self.assertNotEquals(tree.root.getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getdata(), RL_DATA)
        self.assertEquals(tree.root.getleft().getdata(), ROOT_DATA)
        self.assertEquals(tree.root.getright().getdata(), RIGHT_DATA)

    def test_remove_no_child(self):

        def no_rebalance_needed():
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

        def rebalance_needed():
            # These first four tests all test removing one child
            # If any of them fail, removing one child is not working
            self.test_remove_left_left_case()
            self.test_remove_left_right_case()
            self.test_remove_right_right_case()
            self.test_remove_right_left_case()

        no_rebalance_needed()
        rebalance_needed()

    def test_remove_one_child(self):

        def no_rebalance_needed():
            pass

        def rebalance_needed():
            pass

        no_rebalance_needed()
        rebalance_needed()

    def test_remove_two_children(self):

        def no_rebalance_needed():
            pass

        def rebalance_needed():
            pass

        no_rebalance_needed()
        rebalance_needed()

