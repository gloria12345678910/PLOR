import numpy as np
from utils import *

class MODI:

    def __init__(self, transportkostenSaetze, startloesung, startpunktU=0):
        #orange
        self.transportkostenSaetze = np.asarray(transportkostenSaetze)
        #blau NaN is empty
        self.startloesung = np.asarray(startloesung)
        self.u = createEmptyArray(self.transportkostenSaetze.shape[0])
        self.v = createEmptyArray(self.transportkostenSaetze.shape[1])

    def calculateDualvariablen(self, startpunktU=0):
        self.u[startpunktU]=0
        while self.abbruchbedingungCalculateDualvariablen():
            for rowIndex in range(self.transportkostenSaetze.shape[0]):
                for columnIndex in range(self.transportkostenSaetze.shape[1]):
                    if not(np.isnan(self.startloesung[rowIndex, columnIndex])):
                        if not(np.isnan(self.u[rowIndex])):
                            self.v[columnIndex]=self.calculateVGivenU(self.transportkostenSaetze[rowIndex,columnIndex],self.u[rowIndex])
                        if not(np.isnan(self.v[columnIndex])):
                            self.u[rowIndex]= self.calculateUGivenV(self.transportkostenSaetze[rowIndex,columnIndex],self.v[columnIndex])




    def calculateUGivenV(self, c, v):
        return c-v

    def calculateVGivenU(self, c, u):
        return c-u

    def abbruchbedingungCalculateDualvariablen(self):
        # True wenn eins leer, False sonst
        for x in self.u:
            if np.isnan(x):
                return True
        for x in self.v:
            if np.isnan(x):
                return True
        return False

    def calculateOpportunitaetskostensaetze(self):
        self.calculateDualvariablen()
        for rowIndex in range(self.transportkostenSaetze.shape[0]):
            for columnIndex in range(self.transportkostenSaetze.shape[1]):
                if np.isnan(self.startloesung[rowIndex][columnIndex]):
                    self.startloesung[rowIndex][columnIndex]= self.transportkostenSaetze[rowIndex][columnIndex]-self.v[columnIndex]-self.u[columnIndex]


if __name__ == '__main__':
    transportkostenSaetze = [[150,30,110],
                             [80,140,100]]
    startloesung = [[np.nan, 11, 4],
                    [13, np.nan, 2]]

    x = MODI(transportkostenSaetze,startloesung)
    x.calculateOpportunitaetskostensaetze()
    print(x.u)
    print(x.v)
    print( x.startloesung)