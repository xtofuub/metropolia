class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print("Hissi on nyt kerroksessa", self.nykyinen)

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print("Hissi on nyt kerroksessa", self.nykyinen)

    def siirry_kerrokseen(self, kerros):
        if self.nykyinen < kerros:
            while self.nykyinen < kerros:
                self.kerros_ylös()

        elif self.nykyinen > kerros:
            while self.nykyinen > kerros:
                self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


talo = Talo(1, 7, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 3)

print("--- Palohälytys ---")
talo.palohälytys()
