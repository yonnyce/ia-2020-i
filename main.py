from TreeStructs import *


class NumsState(State):

    def addOne(self, state):
        newState = NumsState(state.data + 1)
        return newState

    def getOperations(self) -> []:

        addFunction = Operation('ADD ONE', self.addOne)

        return [addFunction]

    def isSolution(self) -> bool:
        return self.data == 8

    def __str__(self):
        return str(self.data)


class JarrasState(State):

    def getOperations(self) -> []:

        llenarA = Operation('Llenar A', self.llenarA)
        llenarB = Operation('Llenar B', self.llenarB)
        vaciarA = Operation('Vaciar A', self.vaciarA)
        vaciarB = Operation('Vaciar B', self.vaciarB)
        pasarAaB = Operation('Pasar A a B', self.pasarAaB)
        pasarBaA = Operation('Pasar B a A', self.pasarBaA)

        return [llenarA, llenarB, vaciarA, vaciarB, pasarAaB, pasarBaA]

    def isSolution(self) -> bool:
        return self.data['A'] == 4

    def __str__(self):
        return 'A:{0}, B:{1}'.format(self.data['A'], self.data['B'])

    def __hash__(self):
        hash(self.data)

    def llenarA(self, state):
        if(state.data['A'] == 5):
            return None

        newState = JarrasState({'A': 5, 'B': state.data['B']})
        return newState

    def llenarB(self, state):
        if(state.data['B'] == 3):
            return None

        newState = JarrasState({'A': state.data['A'], 'B': 3})
        return newState

    def vaciarA(self, state):
        if(state.data['A'] == 0):
            return None

        newState = JarrasState({'A': 0, 'B': state.data['B']})
        return newState

    def vaciarB(self, state):
        if(state.data['B'] == 0):
            return None
        newState = JarrasState({'A': state.data['A'], 'B': 0})
        return newState

    def pasarAaB(self, state):
        if(state.data['A'] == 0 or state.data['B'] == 3):
            return None

        faltanteB = 3 - state.data['B']

        nuevoB = state.data['B'] + faltanteB if (
            state.data['A']-faltanteB) > 0 else state.data['B'] + state.data['A']

        nuevoA = (
            state.data['A']-faltanteB) if (state.data['A']-faltanteB) > 0 else 0

        # print('A:{},B:{}'.format(nuevoA,nuevoB))
        if nuevoB > 3 or nuevoA < 0:
            return None

        newState = JarrasState({'A': nuevoA, 'B': nuevoB})

        return newState

    def pasarBaA(self, state):
        if(state.data['B'] == 0 or state.data['A'] == 5):
            return None

        faltanteA = 5 - state.data['A']

        nuevoA = state.data['A'] + faltanteA if (
            state.data['B']-faltanteA) > 0 else state.data['A'] + state.data['B']

        nuevoB = (
            state.data['B']-faltanteA) if (state.data['B']-faltanteA) > 0 else 0

        if nuevoA > 5 or nuevoB < 0:
            return None

        newState = JarrasState({'A': nuevoA, 'B': nuevoB})

        return newState


if __name__ == "__main__":
    tree = Tree(Node(JarrasState({'A': 0, 'B': 0})))
    solutionNode = tree.start()
    tree.printSolution()
