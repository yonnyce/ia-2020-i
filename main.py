class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Arist:
    def __init__(self, cost=None, initialNode=None, finalNode=None):
        self.cost = cost
        self.initialNode = initialNode
        self.finalNode = finalNode

    def __str__(self):
        return str(self.initialNode) + "->" + str(self.finalNode) + " " + "[{0}]".format(self.cost)


