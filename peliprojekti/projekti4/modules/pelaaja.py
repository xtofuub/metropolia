class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.saalis = []

    def lisaa_kala(self, kala):
        self.saalis.append(kala)
