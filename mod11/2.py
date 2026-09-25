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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttis = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(120)
polttis.kiihdytä(100)

sahkoauto.kulje(3)
polttis.kulje(3)

print(f"Sähköauto {sahkoauto.rekisteri} matkamittari: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauto {polttis.rekisteri} matkamittari: {polttis.kuljettu_matka} km")
