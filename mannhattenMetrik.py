import numpy as np

from utils import runden


class mannhattenMetrik:

    def __init__(self, bedarf, x, y):
        self.bedarf = bedarf
        self.x = np.asarray([0])
        self.x = np.append(self.x, x)
        self.y = np.asarray([0])
        self.y = np.append(self.y, y)

    def calcDistMatrix(self):
        distMatrix = np.zeros((len(self.bedarf) + 1, len(self.bedarf) + 1))
        for row in range(distMatrix.shape[0]):
            for column in range(distMatrix.shape[1]):
                distMatrix[row][column] = runden(abs(self.x[column] - self.x[row]) + abs(self.y[column] - self.y[row]))
        return distMatrix


if __name__ == '__main__':
    bedarf = np.asarray([3, 2, 1, 3, 2, 4, 2, 3, 2, 1])
    x = np.asarray([-10, -8, -5, -3, 2, 4, 6, 7, 9, 12])
    y = np.asarray([5, -3, 7, 11, -7, -8, 4, 13, -1, -5])
    mannhattenMetrik = mannhattenMetrik(bedarf, x, y).calcDistMatrix()
    print(mannhattenMetrik)
