import numpy as np


class CLSP:

    def __init__(self, demand, matrix):
        if len(demand.shape) > 1:
            raise Exception("Demand muss ein Vector sein")
        if len(matrix.shape) > 2:
            raise Exception("Deine Eingabe ist wahrscheinlich Falsch")

        self.demand = demand
        self.matrix = matrix

        self.q = np.sum(self.matrix * self.demand, axis=1)

    def __call__(self, time_step):
        raise Exception

    def produzierte_menge(self):
        print(f' Q´s: {self.q}')

    def lagerbestand(self):
        timesteps = self.demand.shape[0]
        lagerbestand = np.zeros(timesteps)
        last = 0
        for idx in range(timesteps):
            lagerbestand[idx] = last + self.q[idx] - self.demand[idx]
            last = lagerbestand[idx]
        return lagerbestand


def main():
    demand = np.array([640, 515, 485, 379, 266, 350])
    matrix = np.array([
        [1, 0.5, 0, 0, 0, 0],
        [0, 0.5, 1, 0.3, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.7, 1, 0.5],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0.5],
    ])
    clsp = CLSP(demand, matrix)
    clsp.produzierte_menge()
    print(f' I´s: {clsp.lagerbestand()}')


if __name__ == '__main__':
    main()
