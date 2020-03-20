import abc


class Operation:

    def __init__(self, name, function):
        self.name = name
        self.function = function


class State(abc.ABC):

    def __init__(self, data):
        self.data = data

    def __eq__(self, obj):
        return self.data == obj.data if obj != None and isinstance(obj, State) else False

    @abc.abstractmethod
    def getOperations(self) -> []:
        raise 'getOperations Not implemented get'

    @abc.abstractmethod
    def isSolution(self) -> bool:
        raise 'isSolution Not implemented get'


class Node(abc.ABC):

    parent = None

    def __init__(self, state, operation='None'):
        self.state = state
        self.operation = operation

    def __eq__(self, obj):
        return self.state == obj.state if obj != None and isinstance(obj, Node) else False

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        return hash(self.state)

    def childrensFunc(self) -> []:
        childs = []

        for operation in self.state.getOperations():
            newState = operation.function(self.state)

            if newState is None:
                continue

            newNode = Node(newState, operation.name)

            newNode.parent = self
            childs.append(newNode)

        return childs


class Tree(abc.ABC):

    pendingNodes = []
    solutionNode = None
    visitedNodes = []

    def __init__(self, root: Node = None, deepSearch=False):
        self.root = root
        self.deepSearch = deepSearch

    def start(self):

        self.visitedNodes.append(self.root)
        self.pendingNodes = self.root.childrensFunc()
        self.solutionNode = self.startSearch()
        return self.solutionNode

    def startSearch(self):
        while(len(self.pendingNodes) != 0):
            currentNode = self.pendingNodes.pop() if self.deepSearch else self.pendingNodes.pop(
                0)

            if currentNode in self.visitedNodes:
                continue

            self.visitedNodes.append(currentNode)
            
            if(currentNode.state.isSolution()):
                return currentNode

            self.pendingNodes.extend(currentNode.childrensFunc())

        return None

    def printSolution(self):
        currentNode = self.solutionNode
        solutionSteps = []

        while(currentNode != None):
            solutionSteps.insert(0, currentNode)
            currentNode = currentNode.parent

        for node in solutionSteps:
            print('{1} [{0}] -> '.format(node.state, node.operation), end='')
