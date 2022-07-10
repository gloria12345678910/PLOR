import sys

import numpy as np

class VogelscheApproximationsmethode:

    def __init__(self, matrix, angebot, nachfrage):
        self.matrix = matrix
        self.angebot = angebot
        self.nachfrage = nachfrage

    def calculateDelt(self, direction):
        if direction == 'j':
            matrix = self.matrix.T
        elif direction == 'i':
            matrix = self.matrix
        else:
            raise NotImplementedError("probiere es mal mit den richtigen indizes")
        deltaI = np.empty(0)
        for vector in matrix:
            deltaI = np.append(deltaI, find_nth_smallest(vector, 2) - np.min(vector))
        return deltaI

    def iterationHelper(self, grid, erg, originalMatrix):
        print('-----neue Iteration-----')
        if np.shape(self.matrix)[1] == 1:
            for i in range(len(self.angebot)):
                erg[int(str(grid[i][0]).split('.')[0])][int(str(grid[i][0]).split('.')[1])]=min(self.angebot[i], self.nachfrage[0])
            calculateGesamtkosten(originalMatrix, erg)
        elif np.shape(self.matrix)[0] == 1:
            for i in range(len(self.nachfrage)):
                erg[int(str(grid[i][0]).split('.')[0])][int(str(grid[i][0]).split('.')[1])]=min(self.angebot[0], self.nachfrage[i])
            calculateGesamtkosten(originalMatrix, erg)

        else:
            argmaxDeltaI = np.argmax(self.calculateDelt('i'))
            argmaxDeltaJ = np.argmax(self.calculateDelt('j'))
            maxDeltaI = np.max(self.calculateDelt('i'))
            maxDeltaJ = np.max(self.calculateDelt('j'))
            if maxDeltaJ > maxDeltaI:
                print(f'maxDeltaJ: {maxDeltaJ}')
                pivotElementColumn = argmaxDeltaJ
                pivotElementRow = np.argmin(self.matrix[:, argmaxDeltaJ])
            else:
                print(f'maxDeltaI: {maxDeltaI}')
                pivotElementRow = argmaxDeltaI
                pivotElementColumn = np.argmin(self.matrix[argmaxDeltaI, :])

            angebotPivotElementIndex = pivotElementRow
            nachfragePivotElementIndex = pivotElementColumn
            angebotPivotElement = self.angebot[angebotPivotElementIndex]
            nachfragePivotElement = self.nachfrage[nachfragePivotElementIndex]

            if angebotPivotElement < nachfragePivotElement:
                nachfragePivotElement = nachfragePivotElement - angebotPivotElement
                self.nachfrage[nachfragePivotElementIndex] = nachfragePivotElement

                print(f'PivotElement: {self.matrix[pivotElementRow][pivotElementColumn]}, Index {round(grid[pivotElementRow][pivotElementColumn]+1.1,2)}')
                erg[pivotElementRow][pivotElementColumn]=self.angebot[angebotPivotElementIndex]

                self.angebot = np.delete(self.angebot,angebotPivotElementIndex)
                self.matrix = np.delete(self.matrix,angebotPivotElementIndex, 0)
                grid = np.delete(grid,angebotPivotElementIndex, 0)

            else:
                angebotPivotElement = angebotPivotElement - nachfragePivotElement
                self.angebot[angebotPivotElementIndex] = angebotPivotElement
                print(f'PivotElement: {self.matrix[pivotElementRow][pivotElementColumn]}, Index {round(grid[pivotElementRow][pivotElementColumn]+1.1,2)}')
                erg[pivotElementRow][pivotElementColumn] = self.nachfrage[nachfragePivotElementIndex]
                self.nachfrage = np.delete(self.nachfrage, nachfragePivotElementIndex)
                self.matrix = np.delete(self.matrix, nachfragePivotElementIndex, 1)
                grid = np.delete(grid, nachfragePivotElementIndex, 1)
            return self.iterationHelper(grid,erg,originalMatrix)

    def iteration(self):
        return self.iterationHelper(generateIndexGrid(self.matrix.shape), erg= np.zeros(self.matrix.shape), originalMatrix=self.matrix)

def generateIndexGrid(shape):
    matrix= np.zeros(shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i][j]=float(f'{i}.{j}')
            matrix[i][j]=matrix[i][j]
    return matrix

def find_nth_smallest(a, n):
    return np.partition(a, n - 1)[n - 1]

def calculateGesamtkosten(originalMatrix, erg):
    print(f'erg Matrix:')
    print(erg)
    print(f'Gesamtkosten:')
    print(f'F={calculateGesamtkosten(originalMatrix, erg)}')
    return np.matmul(originalMatrix,erg.T).diagonal().sum()

if __name__ == '__main__':
    matrix = np.array([[150, 30, 110], [80, 140, 100]])
    angebot = np.array([15, 15])
    nachfrage = np.array([13, 11, 6])
    vogelscheApproximationsmethode = VogelscheApproximationsmethode(matrix, angebot, nachfrage)
    vogelscheApproximationsmethode.iteration()

    # matrix = np.array([[18, 16, 12, 20],
    #                    [14, 18, 24, 26],
    #                    [10, 28, 18, 32]])
    # angebot = np.array([70, 100, 80])
    # nachfrage = np.array([60, 90, 40, 60])
    # vogelscheApproximationsmethode = VogelscheApproximationsmethode(matrix, angebot, nachfrage)
    # print(vogelscheApproximationsmethode.iteration())
