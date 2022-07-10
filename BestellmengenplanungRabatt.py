import numpy as np
from utils import runden
from Bestellmengenplanung import Bestellmengenplanung



class Preisliste:
    def __init__(self, auftragsmenge, preisProME):
        # np araay aus Tupel
        # letztes leer wenn bis open end
        self.auftragsmenge = np.asarray(auftragsmenge, dtype=object)
        # np araay
        self.preisProME = np.asarray(preisProME)

    def obereSchranke(self, i):
        if i == len(self.auftragsmenge) - 1:
            return 100000000000
        else:
            return self.auftragsmenge[i][1]

    def untereSchranke(self, i):
        return self.auftragsmenge[i][0]


class BestellmengenplanungRabatt:
    def __init__(self, nachfrage, bestellkosten, preisliste, prozentanteilEinkaufspreises):
        self.preisliste = preisliste
        self.prozentanteilEinkaufspreises = prozentanteilEinkaufspreises
        # bestellkosten= f
        self.bestellkosten = bestellkosten
        # nachfrage= d
        self.nachfrage = nachfrage

    def lagerkosten(self, printOut=1):
        h = np.asarray([])
        for i in range(len(self.preisliste.preisProME)):
            h = np.append(h, runden(self.prozentanteilEinkaufspreises * self.preisliste.preisProME[i],zwischenergebnis=True))
            if printOut:
                print(f'h{i + 1} = {runden(h[i])} in dem Intervall {self.preisliste.auftragsmenge[i]}')
            i += 1
        return h

    def optBestellPolitik(self, printOut=1):
        q = np.asarray([])
        i = 0
        for lagerkosten in self.lagerkosten(printOut=0):
            qi = Bestellmengenplanung(self.nachfrage, self.bestellkosten, lagerkosten).optBestellmenge(printOut=0)
            if printOut:
                print((f'q{i + 1} = {runden(qi)} in dem Intervall {self.preisliste.auftragsmenge[i]}'))
            q = np.append(q, runden(qi,True))
            i += 1
        return q

    def zulaessigkeit(self, printOut=1):
        i = 0
        optBestellmenge = np.asarray([])
        for q in self.optBestellPolitik(printOut=0):
            if q > self.preisliste.obereSchranke(i):
                optBestellmenge = np.append(optBestellmenge,-1)
                if printOut:
                    print(
                        f'q{i + 1}*={runden(q)} ist keine zulässige Lösung, da der Wert q{i + 1}*={runden(q)} nicht im Intervall{self.preisliste.auftragsmenge[i]} liegt.')
            elif (q >= self.preisliste.untereSchranke(i)) and (q <= self.preisliste.obereSchranke(i)):
                optBestellmenge = np.append(optBestellmenge, runden(q,True))
                if printOut:
                    print(
                        f'q{i + 1}*={runden(q)} ist eine zulässige Lösung da der Wert q{i + 1}*={runden(q)} im Intervall{self.preisliste.auftragsmenge[i]} liegt.')
            else:
                if printOut:
                    print(
                        f'q{i + 1}*={runden(q)} ist eine zulässige Lösung, da der Wert q{i + 1}*={runden(q)} kleiner als die untere Schranke ist. Damit nimmt der neue Wert q{i + 1}*={self.preisliste.untereSchranke(i)} an')
                optBestellmenge = np.append(optBestellmenge, runden(self.preisliste.untereSchranke(i),True))
            i += 1
        return optBestellmenge

    def gesamtkosten(self, printOut=1):
        kosten = np.asarray([])
        optBestellmenge = self.zulaessigkeit(printOut=0)
        for i in range(len(optBestellmenge)):
            if round(optBestellmenge[i]) ==-1:
                if printOut:
                    print(f'F(q{i+1}*) entfällt')
                kosten = np.append(kosten, 1000000000000)
            else:
                erg = (self.nachfrage / optBestellmenge[i] )* self.bestellkosten + 0.5 * self.lagerkosten(printOut=0)[i] * optBestellmenge[i] + self.nachfrage * self.preisliste.preisProME[i]
                kosten = np.append(kosten, runden(erg, True))
                if printOut:
                    print(f'F(q{i+1}*)={runden(kosten[i])}')
        return kosten

    def endErg(self):
        minGesamtkosten = np.min(self.gesamtkosten(printOut=0))
        i = np.argmin(self.gesamtkosten(printOut=0))
        optBestellmenge = self.zulaessigkeit(printOut=0)[i]
        print(f'endgültig optimale Bestellmenge: q{i}*={optBestellmenge}')
        print(f'dazugehörige minimale Gesammtkosten: {runden(minGesamtkosten)}')

        anzBestellungen = runden(self.nachfrage/optBestellmenge)
        dauerZwischenZweiBestellungen = runden(optBestellmenge/self.nachfrage)
        print(f'anzahl der Bestellungen: {anzBestellungen}')
        print(f'dauer zwischen zwei Bestellungen: {dauerZwischenZweiBestellungen}')

if __name__ == '__main__':
    preisliste = Preisliste([(1, 9999), (10000, 19999), (20000,)], [0.45, 0.38, 0.35])
    bestellmengenplanungRabatt = BestellmengenplanungRabatt(90000, 90, preisliste, 0.2)
    bestellmengenplanungRabatt.endErg()
