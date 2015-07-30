from node import Node
from bst import Bst


def get_balance_factor(node):
        if node is not None:
            left_height = node.getleft().getheight() if node.getleft() else -1
            right_height = node.getright().getheight() if node.getright() else -1
            balance_factor = left_height - right_height
            return balance_factor

        else:
            return 0


class Avl(Bst):
    """AVL Tree implementation. Values less than or equal to on the left,
    values greater than on the right. Always rebalances itself"""

    def add(self, data):
        """Helper method for adding recursively"""

        def helper_add(data, node):
            if node is None:
                self.size += 1
                return Node(data)
            elif data > node.getdata():
                node.setright(helper_add(data, node.getright()))
                node.determineheight()
                node = self.handle_rotations(node)
                return node
            elif data < node.getdata():
                node.setleft(helper_add(data, node.getleft()))
                node.determineheight()
                node = self.handle_rotations(node)
                return node
            else:
                return node

        self.root = helper_add(data, self.root)

    def remove(self, data):

        def two_children(data, parent, child):
            """For nodes with two children, the predecessor will be used as the replacement"""
            curr = child.getleft()
            prev = None
            while curr.getright():
                prev = curr
                curr = curr.getright()

            replacement = curr
            replacement.setright(child.getright())

            if prev:
                prev.setright(None)
                # Prevents left child from setting itself as its left
                # This will only be called by a rightward descendant of
                # child.getleft()
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

    def handle_rotations(self, parent):
        """If rotations are needed, this function handles them all."""
        if parent is not None:
            if get_balance_factor(parent) is 2:
                child = parent.getleft()
                if get_balance_factor(child) is -1:
                    # Left Right case
                    gchild = child.getright()
                    subtree_a = child.getleft()
                    subtree_b = gchild.getleft()
                    subtree_c = gchild.getright()
                    subtree_d = parent.getright()

                    child.setright(subtree_b)
                    gchild.setleft(child)
                    parent.setleft(gchild)

                # Left Left case
                child = parent.getleft()
                gchild = child.getleft()
                subtree_a = gchild.getleft()
                subtree_b = gchild.getright()
                subtree_c = child.getright()
                subtree_d = parent.getright()

                gchild.setright(subtree_a)
                gchild.setright(subtree_b)
                parent.setleft(subtree_c)
                parent.setright(subtree_d)

                child.setleft(gchild)
                child.setright(parent)

                return child

            elif get_balance_factor(parent) is -2:
                child = parent.getright()
                if get_balance_factor(child) is 1:
                    # Right Left case
                    gchild = child.getleft()
                    subtree_a = parent.getleft()
                    subtree_b = gchild.getleft()
                    subtree_c = gchild.getright()
                    subtree_d = child.getright()

                    child.setleft(subtree_c)
                    gchild.setright(child)
                    parent.setright(gchild)

                # Right Right case
                child = parent.getright()
                gchild = child.getright()
                subtree_a = parent.getleft()
                subtree_b = child.getright()
                subtree_c = gchild.getleft()
                subtree_d = gchild.getright()

                parent.setleft(subtree_a)
                parent.setright(subtree_b)
                gchild.setright(subtree_c)
                gchild.setright(subtree_d)

                child.setleft(parent)
                child.setright(gchild)

                return child

        return parent
