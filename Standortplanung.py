import numpy as np

class Standortplanung:

    def __init__(self, d, t):
        self.d = d
        if t.shape[0] != t.shape[1] or len(t.shape) > 2:
            raise Exception("Gib halt richtig ein")
        self.t = t

    def standortplanung(self):
        regionen_cnt = self.d.shape[0]
        lager_cnt = self.d.shape[1]

        c = np.zeros(self.d.shape)
        for rowIdx in range(regionen_cnt):
            for colIdx in range(lager_cnt):
                sum = 0
                for region in range(regionen_cnt):
                    sum += self.t[rowIdx, region] + self.t[region, rowIdx]
                c[rowIdx, colIdx] = self.d[rowIdx, colIdx] * sum
        print(c)

def main():
    d = np.array([
        [1, 61, 29],
        [143, 1, 97],
        [87, 122, 1],
        [33, 95, 100],
        [127, 111, 144],
        [111, 69, 136],
        [24, 38, 92]
    ])

    t = np.array([
        [0, 55, 54, 67, 58, 48, 22],
        [40, 0, 35, 22, 23, 77, 66],
        [31, 68, 0, 70, 69, 50, 73],
        [39, 40, 64, 0, 70, 48, 46],
        [25, 18, 68, 27, 0, 74, 48],
        [25, 18, 24, 39, 25, 0, 69],
        [35, 76, 71, 29, 83, 41, 0]
    ])
    sop = Standortplanung(d, t)
    print(sop.standortplanung())

if __name__ == '__main__':
    main()
