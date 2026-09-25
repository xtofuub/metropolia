import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteri = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, kiihty):
        self.nopeus = self.nopeus + kiihty

        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntia):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tuntia


autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


while True:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)

    for auto in autot:
        auto.kulje(1)

    kilpailu_loppui = False

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppui = True

    if kilpailu_loppui:
        break


print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")
print("-" * 55)

for auto in autot:
    print(
        auto.rekisteri,
        "|",
        auto.huippunopeus,
        "km/h |",
        auto.nopeus,
        "km/h |",
        auto.kuljettu_matka,
        "km"
    )