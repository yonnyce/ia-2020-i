import abc
import operator


class Operation:
    """
    Represent a operation that can be applied over a state
    """

    def __init__(self, name, function, cost=0):
        """
            Args:
                name: The name of operation
                function: Function that will be applied over a state
                cost: Cost of operation
        """
        self.name = name
        self.function = function
        self.cost = cost

    def __str__(self):
        return self.name + '({})'.format(str(self.cost))


class State(abc.ABC):
    """
    Represents a state of the problem
    """

    def __init__(self, data):
        self.data = data

    def __eq__(self, obj):
        return self.data == obj.data if obj != None and isinstance(obj, State) else False

    @abc.abstractmethod
    def getOperations(self) -> []:
        """
            Returns the list of functions that represents all operations that can be applied over a state
        """
        raise 'getOperations Not implemented get'

    @abc.abstractmethod
    def isSolution(self) -> bool:
        """
            Returns True if the current state is a solution of the problem
        """
        raise 'isSolution Not implemented get'


class Node(abc.ABC):
    """
    Contain the necesary logic for create and associate new states in a search problem
    """

    def __init__(self, state, operation=Operation('None', None), parent=None):
        """
        Args:
            state: State representation of the problem
            operation: Operation that was applied over parent for create the getted state
            parent: parent of the current state
        """
        self.state = state
        self.operation = operation
        self.parent = parent
        # here asign the acumulation of costs
        self.acumCost = parent.acumCost+operation.cost if parent != None else 0

    def __eq__(self, obj):
        return self.state == obj.state if obj != None and isinstance(obj, Node) else False

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        return hash(self.state)

    def childrensFunc(self) -> []:
        """
        Generate new states appling the actions definied in the state
        """
        childs = []

        # Applicate each operation definied in the state for generate new states
        for operation in self.state.getOperations():
            newState = operation.function(self.state)

            # ignore if the state is None
            if newState is None:
                continue

            newNode = Node(newState, operation, self)

            childs.append(newNode)

        return childs


class Tree(abc.ABC):
    """
    Structural representetion of a Tree, with functions for search in a node spaces
    """

    pendingNodes = []
    solutionNode = None
    visitedNodes = set()

    def __init__(self, root: Node = None, depthSearch=False, uniformCost=False):
        """
        Initialization of the Tree

            Args:
                root: A initial Node that represent the start state
                depthSearch: Indicate if the search will be depth-first, defaults is breadth 
                uniformCost: Indicate if the search will be uniform cost approach
        """
        self.root = root
        self.depthSearch = depthSearch if not uniformCost else False
        self.uniformCost = uniformCost

    def start(self):
        """
        Start the search and construction of the Tree
        """
        self.movements = 0
        self.visitedNodes.add(self.root)
        self.pendingNodes = self.root.childrensFunc()
        self.solutionNode = self.startSearch()
        return self.solutionNode

    def startSearch(self):
        """
        Implement the principal loop of search, creating and evaluationg each node
        """

        while(len(self.pendingNodes) != 0):
            currentNode = self.pendingNodes.pop() if self.depthSearch else self.pendingNodes.pop(
                0)

            # Skip if the current node are visited before (this comportament will change when implement A*)
            if currentNode in self.visitedNodes:
                continue

            self.visitedNodes.add(currentNode)

            # Evaluate if the current node is the solution
            if(currentNode.state.isSolution()):
                return currentNode

            # Add new nodes to the pending Nodes
            self.pendingNodes.extend(currentNode.childrensFunc())

            if self.uniformCost:
                self.pendingNodes.sort(key=operator.attrgetter('acumCost'))

            self.movements += 1

        return None

    def printSolution(self):
        """Print all solution path if exist"""

        currentNode = self.solutionNode
        solutionSteps = []

        print('Total evaluated states: {}'.format(self.movements))

        while(currentNode != None):
            solutionSteps.insert(0, currentNode)
            currentNode = currentNode.parent

        for node in solutionSteps:
            print('<{2}> {1} [{0}] -> '.format(str(node.state),
                                               str(node.operation), str(node.acumCost)), end='')
