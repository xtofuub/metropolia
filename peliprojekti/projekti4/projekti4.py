import random


class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    def __init__(self, nimi, kalat):
        self.nimi = nimi
        self.kalat = kalat


class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.saalis = []

    def lisaa_kala(self, kala):
        self.saalis.append(kala)


def nayta_valikko():
    print("\n--- KALAREISSU ---")
    print("1. Kalasta")
    print("2. Vaihda paikkaa")
    print("3. Näytä saalis")
    print("4. Lopeta")


def kalasta(pelaaja):
    kala = random.choice(pelaaja.sijainti.kalat)
    print("\nHeität ongen...")
    print("Sait:", kala.nimi)
    print("Paino:", kala.paino, "kg")

    vastaus = input("Pidätkö kalan? (k/e): ")

    if vastaus.lower() == "k":
        pelaaja.lisaa_kala(kala)
        print("Kala lisättiin saaliiseen.")
    else:
        print("Kala vapautettiin.")


def nayta_saalis(pelaaja):
    print("\n--- SAALIS ---")

    if len(pelaaja.saalis) == 0:
        print("Saalis on tyhjä.")
        return

    for kala in pelaaja.saalis:
        print(kala.nimi, "-", kala.paino, "kg")


def main():
    print("Tervetuloa kalareissulle!")

    nimi = input("Mikä on nimesi? ")
    ika = int(input("Minkä ikäinen olet? "))

    ahven = Esine("Ahven", 0.8)
    särki = Esine("Särki", 0.5)
    taimen = Esine("Taimen", 2.1)

    lampi = Huone("Lampi", [ahven, särki])
    joki = Huone("Joki", [taimen, ahven])

    pelaaja = Pelaaja(nimi, ika, lampi)

    while True:
        print("\nOlet paikassa:", pelaaja.sijainti.nimi)
        nayta_valikko()

        valinta = input("Valinta: ")

        if valinta == "1":
            kalasta(pelaaja)
        elif valinta == "3":
            nayta_saalis(pelaaja)
        elif valinta == "4":
            print("Kiitos pelaamisesta!")
            break
        else:
            print("Tämä toiminto ei ole vielä valmis.")


main()
