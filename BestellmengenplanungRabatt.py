import numpy as np

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
            h = np.append(h, self.prozentanteilEinkaufspreises * self.preisliste.preisProME[i])
            if printOut:
                print(f'h{i + 1} = {round(h[i] * 10000) / 10000} in dem Intervall {self.preisliste.auftragsmenge[i]}')
            i += 1
        return h

    def optBestellPolitik(self):
        q = np.asarray([])
        i = 0
        for lagerkosten in self.lagerkosten(printOut=0):
            qi = Bestellmengenplanung(self.nachfrage, self.bestellkosten, lagerkosten).optBestellmenge(printOut=0)
            print((f'q{i + 1} = {round(qi * 10000) / 10000} in dem Intervall {self.preisliste.auftragsmenge[i]}'))
            q = np.append(q, qi)
            i += 1
        return q

    def zulaessigkeit(self):
        i = 0
        optBestellmenge = np.asarray([])
        for q in self.optBestellPolitik():
            if q > self.preisliste.obereSchranke(i):
                print(
                    f'q{i + 1}*={q} ist keine zulässige Lösung, da der Wert q{i + 1}*={q} nicht im Intervall{self.preisliste.auftragsmenge[i]} liegt.')
            elif (q >= self.preisliste.untereSchranke(i)) and (q <= self.preisliste.obereSchranke(i)):
                optBestellmenge = np.append(optBestellmenge, q)
                print(
                    f'q{i + 1}*={q} ist eine zulässige Lösung da der Wert q{i + 1}*={q} im Intervall{self.preisliste.auftragsmenge[i]} liegt.')
            else:
                print(
                    f'q{i + 1}*={q} ist eine zulässige Lösung, da der Wert q{i + 1}*={q} kleiner als die untere Schranke ist. Damit nimmt der neue Wert q{i + 1}*={self.preisliste.untereSchranke(i)} an')
                optBestellmenge = np.append(optBestellmenge, self.preisliste.untereSchranke(i))
            i += 1
        return optBestellmenge


if __name__ == '__main__':
    preisliste = Preisliste([(1, 9999), (10000, 19999), (20000,)], [0.45, 0.38, 0.35])
    bestellmengenplanungRabatt = BestellmengenplanungRabatt(90000, 90, preisliste, 0.2)
    bestellmengenplanungRabatt.zulaessigkeit()
