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


h = Hissi(1, 7)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
