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

    def produzierte_menge(self, time_step):
        if time_step <= 0:
            raise Exception("Timestep muss mindestens 1 sein")
        print(self.q)
        return self.q[time_step - 1]

    def lagerbestand(self):
        timesteps = self.demand.shape[0]
        lagerbestand = np.zeros(timesteps)
        last = 0
        for idx in range(timesteps):
            lagerbestand[idx] = last + self.q[idx] - self.demand[idx]
            last = lagerbestand[idx]
        return lagerbestand



def main():
    demand = np.array([20, 20, 20, 15, 15])
    matrix = np.array([
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    clsp = CLSP(demand, matrix)
    print(clsp.produzierte_menge(4))
    print(clsp.lagerbestand())


if __name__ == '__main__':
    main()
