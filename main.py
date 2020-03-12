class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, a, b, cost):
        self.initialVertex = a
        self.finalVertex = b
        self.cost = cost

    def __str__(self):
        return str(self.initialVertex) + ' -> ' + str(self.finalVertex) + '[{0}]'.format(self.cost)


class Graph:

    def __init__(self, edges=[], isDirected=False):
        self.isDirected = isDirected
        self.edges = []
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge):

        if edge not in self.edges:
            self.edges.append(edge)

        if self.isDirected:
            inverseCost = edge.cost
            inverseEdge = Edge(
                edge.finalVertex, edge.initialVertex, inverseCost)
            self.edges.append(inverseEdge)

    def printGraph(self):
        for edge in self.edges:
            print(edge)


if __name__ == "__main__":

    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')

    edges = [Edge(a, b, 10), Edge(b, c, 15), Edge(c, a, 35)]

    graph = Graph(edges, False)

    graph.printGraph()
