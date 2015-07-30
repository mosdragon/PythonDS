from node import Node
import unittest


class NodeTester(unittest.TestCase):
    
    def test_init(self):
        startdata = 100
        root = Node(startdata)
        self.assertEqual(root.getheight(), 0)
        self.assertEqual(root.getdata(), startdata)
        self.assertIsNone(root.getleft())
        self.assertIsNone(root.getright())


    def test_setting_leaf_nodes(self):
        parent_data = 10
        parent = Node(parent_data)

        self.assertEqual(parent.getheight(), 0)

        left_child = Node(5)
        right_child = Node(20)

        parent.setleft(left_child)
        self.assertEqual(parent.getheight(), 1)

        parent.setright(right_child)
        self.assertEqual(parent.getheight(), 1)

        parent.setleft(None)
        self.assertEqual(parent.getheight(), 1)

        parent.setright(None)
        self.assertEqual(parent.getheight(), 0)

        # Parent no longer has any children nodes

        # Left child node gets two children added
        left_gchild = Node(4)
        right_gchild = Node(6)
        left_child.setleft(left_gchild)
        left_child.setright(right_gchild)
        self.assertEqual(left_child.getheight(), 1)

        # Parent gets left_child as its child
        parent.setleft(left_child)
        self.assertEqual(parent.getheight(), left_child.getheight() + 1)


    def test_determineheight(self):
        
        left_child = Node(5)
        self.assertEqual(left_child.getheight(), 0) 
        
        left_child.height = 4
        self.assertEqual(left_child.getheight(), 4)

        right_child = Node(20)
        self.assertEqual(right_child.getheight(), 0)

        parent = Node(10)
        parent.setright(right_child)
        self.assertEqual(parent.getheight(), 1)
        
        parent.setleft(left_child)
        self.assertEqual(parent.getheight(), left_child.getheight() + 1)

        left_child = None
        parent.setleft(None)
        self.assertEqual(parent.getheight(), right_child.getheight() + 1)

        left_child = Node(5)
        parent.setleft(left_child)

        self.assertEqual(parent.getheight(), left_child.getheight() + 1)
        self.assertEqual(parent.getheight(), right_child.getheight() + 1)


        # These will be the children of left_child
        left_gchild = Node(15)
        right_gchild = Node(25)
        left_child.setleft(left_gchild)
        left_child.setleft(right_gchild)

        self.assertEqual(left_child.getheight(), left_gchild.getheight() + 1)

        # Parent height will be unchanged despite child's height changing
        # Until the parent calls determineheight() function
        self.assertEqual(parent.getheight(), right_child.getheight() + 1)
        self.assertNotEqual(parent.getheight(), left_child.getheight() + 1)

        # Now call determineheight() on parent. It will not have the height of
        # left_child height plus 1
        parent.determineheight()
        self.assertEqual(parent.getheight(), left_child.getheight() + 1)
        self.assertNotEqual(parent.getheight(), right_child.getheight() + 1)


    def test_equality(self):
        data = 10
        original = Node(data)
        duplicate = Node(data)

        self.assertEqual(original, duplicate)

        left_child = Node(5)

        original.setleft(left_child)

        self.assertNotEqual(original, duplicate)

        duplicate.setleft(left_child)
        self.assertEqual(original, duplicate)

        # Demonstrate that nodes equal despite having different left and right children

        duplicate.setleft(None)
        right_child = left_child
        duplicate.setright(right_child)
        self.assertEqual(original, duplicate)
