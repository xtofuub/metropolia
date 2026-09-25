class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0


auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton nopeus: {auto.nopeus}")

auto.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus}")
