import abc
import operator


class Operation:

    def __init__(self, name, function, cost=0):
        self.name = name
        self.function = function
        self.cost = cost

    def __str__(self):
        return self.name + '({})'.format(str(self.cost))


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

    def __init__(self, state, operation=Operation('None', None), parent=None):
        self.state = state
        self.operation = operation
        self.parent = parent
        self.acumCost = parent.acumCost+operation.cost if parent != None else 0

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

            newNode = Node(newState, operation, self)

            childs.append(newNode)

        return childs


class Tree(abc.ABC):

    pendingNodes = []
    solutionNode = None
    visitedNodes = set()

    def __init__(self, root: Node = None, deepSearch=False, uniformCost=False):
        self.root = root
        self.deepSearch = deepSearch if not uniformCost else False
        self.uniformCost = uniformCost

    def start(self):
        self.movements = 0
        self.visitedNodes.add(self.root)
        self.pendingNodes = self.root.childrensFunc()
        self.solutionNode = self.startSearch()
        return self.solutionNode

    def startSearch(self):
        while(len(self.pendingNodes) != 0):
            currentNode = self.pendingNodes.pop() if self.deepSearch else self.pendingNodes.pop(
                0)

            if currentNode in self.visitedNodes:
                continue

            self.visitedNodes.add(currentNode)

            if(currentNode.state.isSolution()):
                return currentNode

            self.pendingNodes.extend(currentNode.childrensFunc())

            if self.uniformCost:
                self.pendingNodes.sort(key=operator.attrgetter('acumCost'))

            self.movements += 1

        return None

    def printSolution(self):
        currentNode = self.solutionNode
        solutionSteps = []

        print('Total evaluated states: {}'.format(self.movements))

        while(currentNode != None):
            solutionSteps.insert(0, currentNode)
            currentNode = currentNode.parent

        for node in solutionSteps:
            print('<{2}> {1} [{0}] -> '.format(str(node.state),
                                               str(node.operation), str(node.acumCost)), end='')
