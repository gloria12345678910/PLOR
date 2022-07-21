import numpy as np


class savingsAlgorithmus:

    def __init__(self, distMatrix, i=0):
        self.distMatrix = distMatrix
        self.i = i

    def savingsMatrix(self):
        savingsMatrix = np.zeros((self.distMatrix.shape[0] - 1, self.distMatrix.shape[1] - 1))
        for row in range(self.distMatrix.shape[0]):
            for column in range(self.distMatrix.shape[1]):
                if row > 0 and column > 0 and column != row:
                    savingsMatrix[row - 1][column - 1] = self.distMatrix[0][row] + self.distMatrix[0][column] - \
                                                         self.distMatrix[row][column]
        print(f'der größte savingswert ist : {np.max(savingsMatrix)}')
        return savingsMatrix


if __name__ == '__main__':
    matrix = np.array([[0, 25, 8, 18], [25, 0, 13, 10], [8, 13, 0, 12], [18, 10, 12, 0]])
    print(savingsAlgorithmus(matrix).savingsMatrix())
