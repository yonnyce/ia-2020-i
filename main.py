class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Vertex:
    def __init__(self, name, neighbours=None):
        self.name = name

        if neighbours != None:
            self.neighbours = list()
        else:
            self.neighbours = neighbours

    def addNeighbour(self, v):

        if v not in self.neighbours:
            self.neighbours.append(v)


class Edge:
    def __init__(self, a, b, cost):
        self.initialVertex = a
        self.finalVertex = b
        self.cost = cost


class Graph:
    vertex = {}
    isDirected = False

    def addEdge(self, a, b, cost1, cost2):

        if a in self.vertex and b in self.vertex:
            self.vertex[a].addNeighbour(b)

            if not self.isDirected:
                self.vertex[b].addNeighbour(a)
