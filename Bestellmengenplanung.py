import math


class Bestellmengenplanung:

    def __init__(self, nachfrage, kostenProBestellung, lagerkostenProMengeundZeiteinheit):
        self.lagerkostenProMengeundZeiteinheit = lagerkostenProMengeundZeiteinheit
        self.kostenProBestellung = kostenProBestellung
        self.nachfrage = nachfrage

    def optBestellmenge(self):
        return math.sqrt((2 * self.nachfrage * self.kostenProBestellung) / self.lagerkostenProMengeundZeiteinheit)

    def anzBestellungenProJahr(self):
        return self.nachfrage/self.optBestellmenge()

    def zyklusdauer(self):
        return self.optBestellmenge()/self.nachfrage

    def bestellkosten(self):
        return self.nachfrage/self.optBestellmenge()*self.kostenProBestellung

    def jaehrlicheLagerkosten(self):
        return 0.5*self.lagerkostenProMengeundZeiteinheit*self.optBestellmenge()

    def zielfunktionGesamtkosten(self):
        return self.nachfrage/self.optBestellmenge()*self.kostenProBestellung+0.5*self.lagerkostenProMengeundZeiteinheit*self.kostenProBestellung