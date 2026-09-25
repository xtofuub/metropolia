class Auto:
    def __init__(self, reskisteritunnus, huippunopeus):
        self.rekisteritunnus = reskisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0


auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")

print(f"Huippunopeus: {auto.huippunopeus}")
print(f"nopeus: {auto.nopeus}")
print(f"kuljettu: {auto.kuljettu}")

