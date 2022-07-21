import math

from utils import runden


class Bestellmengenplanung:
    def __init__(self, nachfrage, bestellkosten, lagerkosten):
        #lagerkosten= h
        self.lagerkosten = lagerkosten
        #bestellkosten= f
        self.bestellkosten = bestellkosten
        #nachfrage= d
        self.nachfrage = nachfrage

    def optBestellmenge(self, printOut = 1):
        erg= math.sqrt((2 * self.nachfrage * self.bestellkosten) / self.lagerkosten)
        if printOut:
            print(f'q*={erg}')
        return runden(erg,True)

    def anzBestellungen(self, printOut=1):
        anzBestellungen= self.nachfrage/self.optBestellmenge(printOut=0)
        if printOut:
            print(f'anzahl Bestellungen pro Jahr={anzBestellungen}')
        return runden(anzBestellungen,True)

    def tageZwischenZweiBestellungen(self):
        print(f'Tage zwischen 2 Bestellungen:    {365/runden(self.anzBestellungen(printOut=0),zwischenergebnis=True)}')

    def zyklusdauer(self):
        #zyklusdauer= Zeit zwischen den Bestellungen
        zyklusdauer=self.optBestellmenge(printOut=0)/self.nachfrage
        print(f'zyklusdauer ( Zeit zwischen den Bestellungen) ={zyklusdauer}')
        return runden(zyklusdauer,True)

    def jaehrlicheBestellkosten(self):
        jaehrlicheBestellkosten=self.nachfrage/self.optBestellmenge(printOut=0)*self.bestellkosten
        print(f'jearliche Bestellkosten={jaehrlicheBestellkosten}')
        return runden(jaehrlicheBestellkosten,True)

    def jaehrlicheLagerkosten(self):
        jearlicheLagerkosten= 0.5 * self.lagerkosten * self.optBestellmenge(printOut=0)
        print(f'jearlicheLagerkoster ={jearlicheLagerkosten}')
        return runden(jearlicheLagerkosten,True)

    def gesamtkosten(self):
        gesamtkosten=(self.nachfrage / self.optBestellmenge(printOut=0)) * self.bestellkosten + 0.5 * self.lagerkosten * self.optBestellmenge()
        print(f'gesamtkosten={gesamtkosten}')
        return runden(gesamtkosten,True)

    def calculateAll(self):
        self.optBestellmenge()
        self.anzBestellungen()
        self.zyklusdauer()
        self.jaehrlicheBestellkosten()
        self.jaehrlicheLagerkosten()
        self.gesamtkosten()
        self.tageZwischenZweiBestellungen()


if __name__ == '__main__':
    bestellmengenplanung = Bestellmengenplanung(lagerkosten=18,bestellkosten=69,nachfrage=1223)
    bestellmengenplanung.calculateAll()
