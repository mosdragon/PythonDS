
class Node:
    """This is a node class that can hold a left child and a right child"""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 0


    def determineheight(self):

        left_height = self.getleft().getheight() if self.getleft() else -1
        right_height = self.getright().getheight() if self.getright() else -1
        self.height = max(left_height, right_height) + 1

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

    def __eq__(self, other):
        """Equality of nodes only depends on the data and the height of the nodes"""

        if isinstance(other, self.__class__):
            match = (self.getdata() == other.getdata()
                and self.getheight() == other.getheight())
            return match
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        template = "DATA: {}\t" + "HEIGHT: {}"
        return str.format(template, self.data, self.height)


