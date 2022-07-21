class dualisierung:

    def __init__(self, minF, nb):
        self.minF = minF
        self.nb = nb

    def printItOut(self):
        for ergLine in range(len(self.nb[0].const)):
            line = ""
            for ergConst in range(len(self.nb)):
                number = self.nb[ergConst].const[ergLine]
                if number>0 and ergConst>0:
                    strNumber = "+" + str(number)
                else:
                    strNumber = str(number)
                line += strNumber + " w" + str(ergConst+1) + " "
            line += " <= " + str(self.minF[ergLine])
            print(line)
        ergMax= ""
        for nebenbedingung in range(len(self.nb)):
            if self.nb[nebenbedingung].erg > 0 and nebenbedingung > 0:
                strNumber = "+" + str(self.nb[nebenbedingung].erg)
            else:
                strNumber = str(self.nb[nebenbedingung].erg)
            ergMax += strNumber + " w" + str(nebenbedingung + 1) + " "
        print("max = " + ergMax)

class nb:

    def __init__(self, const, erg, isGreaterThan):
        if not isGreaterThan:
            for i in range(len(const)):
                const[i] *= -1
            erg *= -1
        self.const = const
        self.erg = erg
        self.isGreaterThan = isGreaterThan


if __name__ == '__main__':
    nebenbedingung = [nb([1, -8, 4], -1, False), nb([-6, -4, 4], 6, True)]
    dualisierung = dualisierung([-6, -1, 3],nebenbedingung)
    dualisierung.printItOut()
