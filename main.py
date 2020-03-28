from TreeStructs import *
from copy import copy, deepcopy


class PuzzleState(State):
    def getOperations(self) -> []:
        moverArriba = Operation('Arriba', self.moveUp, 1)
        moverAbajo = Operation('Abajo', self.moveDown, 1)
        moverDerecha = Operation('Derecha', self.moveRight, 1)
        moverIzquierda = Operation('Izquierda', self.moveLeft, 1)

        return [moverArriba, moverAbajo, moverDerecha, moverIzquierda]

    def isSolution(self) -> bool:
        return self.data == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def findVoidIndex(self, state):
        for i in range(0, len(state.data)):
            for j in range(0, len(state.data[i])):
                if(state.data[i][j] == 0):
                    return [i, j]

    def validMovement(self, state, i, j):
        valid = True

        if(i >= len(state.data)):
            valid = False

        if(i < 0):
            valid = False

        if(j >= len(state.data[0])):
            valid = False

        if(j < 0):
            valid = False

        return valid

    def moveUp(self, state):
        newState = self.move(state, -1, 0)
        return newState

    def moveDown(self, state):
        newState = self.move(state, 1, 0)
        return newState

    def moveRight(self, state):
        newState = self.move(state, 0, 1)
        return newState

    def moveLeft(self, state):
        newState = self.move(state, 0, -1)
        return newState

    def move(self, state, addI, addJ):
        voidIndexArray = self.findVoidIndex(state)
        i = voidIndexArray[0]
        j = voidIndexArray[1]

        newI = i + addI
        newJ = j + addJ

        if(not self.validMovement(state, newI, newJ)):
            return None

        newData = deepcopy(state.data)

        newData[i][j] = newData[newI][newJ]
        newData[newI][newJ] = 0

        return PuzzleState(newData)

    def __str__(self):
        string = '\n'
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                string += str(self.data[i][j])+' '
            string += '\n'

        string += '\n'
        return string

    def __hash__(self):
        return hash(str(self))


if __name__ == "__main__":
    initialNode = Node(PuzzleState([[1, 2, 5], [3, 4, 8], [6, 7, 0]]))
    tree = Tree(initialNode, False, False)
    solutionNode = tree.start()
    tree.printSolution()
