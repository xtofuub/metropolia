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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.nimi}, pituus: {self.pituus} km")
        print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")
        print("-" * 55)
        for auto in self.autot:
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

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        print(f"--- Tunti {tunti} ---")
        kilpailu.tulosta_tilanne()

print(f"--- Kilpailu päättyi! Aikaa kului {tunti} tuntia ---")
kilpailu.tulosta_tilanne()
