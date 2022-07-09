import math


class Bestellmengenplanung:
    def __init__(self, nachfrage, bestellkosten, lagerkosten):
        #lagerkosten= h
        self.lagerkosten = lagerkosten
        #bestellkosten= f
        self.bestellkosten = bestellkosten
        #nachfrage= d
        self.nachfrage = nachfrage
        self.calculateAll()

    def optBestellmenge(self, printOut = 1):
        erg= math.sqrt((2 * self.nachfrage * self.bestellkosten) / self.lagerkosten)
        if printOut:
            print(f'q*={erg}')
        return erg

    def anzBestellungen(self, printOut=1):
        anzBestellungen= self.nachfrage/self.optBestellmenge(printOut=0)
        if printOut:
            print(f'anzahl Bestellungen={anzBestellungen}')
        return anzBestellungen

    def anzBestellungenProJahr(self):
        anzBestellungenProJahr = self.anzBestellungen(printOut=0)*356
        print(f'anz Bestellungen Pro Jahr={anzBestellungenProJahr}')
        return anzBestellungenProJahr

    def zyklusdauer(self):
        #zyklusdauer= Zeit zwischen den Bestellungen
        zyklusdauer=self.optBestellmenge(printOut=0)/self.nachfrage
        print(f'zyklusdauer ( Zeit zwischen den Bestellungen) ={zyklusdauer}')
        return zyklusdauer

    def jaehrlicheBestellkosten(self):
        jaehrlicheBestellkosten=self.nachfrage/self.optBestellmenge(printOut=0)*self.bestellkosten
        print(f'jearliche Bestellkosten={jaehrlicheBestellkosten}')
        return jaehrlicheBestellkosten

    def jaehrlicheLagerkosten(self):
        jearlicheLagerkosten= 0.5 * self.lagerkosten * self.optBestellmenge(printOut=0)
        print(f'jearlicheLagerkoster ={jearlicheLagerkosten}')
        return jearlicheLagerkosten

    def gesamtkosten(self):
        gesamtkosten=(self.nachfrage / self.optBestellmenge(printOut=0)) * self.bestellkosten + 0.5 * self.lagerkosten * self.optBestellmenge()
        print(f'gesamtkosten={gesamtkosten}')
        return gesamtkosten

    def calculateAll(self):
        self.optBestellmenge()
        self.anzBestellungen()
        self.anzBestellungenProJahr()
        self.zyklusdauer()
        self.jaehrlicheBestellkosten()
        self.jaehrlicheLagerkosten()
        self.gesamtkosten()


if __name__ == '__main__':
    bestellmengenplanung = Bestellmengenplanung(1500,15,0.15)
