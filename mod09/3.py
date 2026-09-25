class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 2000

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, matka):
        self.kuljettu += self.nopeus * matka 


auto = Auto("ABC-123", 142)

auto.nopeus = 60
auto.kulje(2)
print(f"kuljettu matka: {auto.kuljettu} km")