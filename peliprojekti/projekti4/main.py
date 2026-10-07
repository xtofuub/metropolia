import json
import random

from modules.esine import Esine
from modules.huone import Huone
from modules.pelaaja import Pelaaja


def nayta_valikko():
    print("\n--- KALAREISSU ---")
    print("1. Kalasta")
    print("2. Vaihda paikkaa")
    print("3. Näytä saalis")
    print("4. Tallenna peli")
    print("5. Lataa peli")
    print("6. Lopeta")


def kalasta(pelaaja):
    kala = random.choice(pelaaja.sijainti.kalat)

    print("\nHeität ongen...")
    print("Sait:", kala.nimi)
    print("Paino:", kala.paino, "kg")

    vastaus = input("Pidätkö kalan? (k/e): ")

    if vastaus.lower() == "k":
        pelaaja.lisaa_kala(kala)
        print("Kala lisättiin saaliiseen.")
        return True

    print("Kala vapautettiin.")
    return False


def vaihda_paikkaa(pelaaja, paikat):
    print("\nKalastuspaikat:")

    for numero, paikka in enumerate(paikat, 1):
        print(numero, paikka.nimi)

    valinta = input("Valitse paikka: ")

    if valinta.isdigit():
        numero = int(valinta)

        if 1 <= numero <= len(paikat):
            pelaaja.sijainti = paikat[numero - 1]
            print("Siirryit paikkaan:", pelaaja.sijainti.nimi)
            return True

    print("Väärä valinta.")
    return False


def nayta_saalis(pelaaja):
    print("\n--- SAALIS ---")

    if len(pelaaja.saalis) == 0:
        print("Saalis on tyhjä.")
        return 0

    paino = 0

    for kala in pelaaja.saalis:
        print(kala.nimi, "-", kala.paino, "kg")
        paino += kala.paino

    print("Yhteensä:", paino, "kg")
    return len(pelaaja.saalis)


def tallenna_peli(pelaaja, tiedosto):
    tiedot = {
        "nimi": pelaaja.nimi,
        "ika": pelaaja.ika,
        "sijainti": pelaaja.sijainti.nimi,
        "saalis": []
    }

    for kala in pelaaja.saalis:
        tiedot["saalis"].append(kala.nimi)

    with open(tiedosto, "w", encoding="utf-8") as tiedosto:
        json.dump(tiedot, tiedosto, ensure_ascii=False, indent=4)

    print("Peli tallennettu.")
    return True


def lataa_peli(paikat, kalat, tiedosto):
    try:
        with open(tiedosto, "r", encoding="utf-8") as tiedosto:
            tiedot = json.load(tiedosto)
    except FileNotFoundError:
        print("Tallennettua peliä ei löytynyt.")
        return None

    sijainti = paikat[0]

    for paikka in paikat:
        if paikka.nimi == tiedot["sijainti"]:
            sijainti = paikka

    pelaaja = Pelaaja(tiedot["nimi"], tiedot["ika"], sijainti)

    for kalan_nimi in tiedot["saalis"]:
        if kalan_nimi in kalat:
            pelaaja.lisaa_kala(kalat[kalan_nimi])

    print("Peli ladattu.")
    return pelaaja


def main():
    print("Tervetuloa kalareissulle!")

    ahven = Esine("Ahven", 0.8)
    särki = Esine("Särki", 0.5)
    taimen = Esine("Taimen", 2.1)
    hauki = Esine("Hauki", 3.4)
    lohi = Esine("Lohi", 4.2)

    lampi = Huone("Lampi", [ahven, särki])
    joki = Huone("Joki", [taimen, hauki])
    meri = Huone("Meri", [lohi, hauki])

    paikat = [lampi, joki, meri]

    kalat = {
        "Ahven": ahven,
        "Särki": särki,
        "Taimen": taimen,
        "Hauki": hauki,
        "Lohi": lohi
    }

    nimi = input("Mikä on nimesi?: ")

    while True:
        try:
            ika = int(input("Minkä ikäinen olet?: "))
            break
        except ValueError:
            print("Anna ikä numerona.")

    pelaaja = Pelaaja(nimi, ika, lampi)

    while True:
        print("\nOlet paikassa:", pelaaja.sijainti.nimi)
        nayta_valikko()

        valinta = input("Valinta: ")

        if valinta == "1":
            kalasta(pelaaja)

            if len(pelaaja.saalis) >= 3:
                print("\nSait kolme kalaa!")
                print("Onneksi olkoon,", pelaaja.nimi + "!")
                break

        elif valinta == "2":
            vaihda_paikkaa(pelaaja, paikat)

        elif valinta == "3":
            nayta_saalis(pelaaja)

        elif valinta == "4":
            tallenna_peli(pelaaja, "tallennus.json")

        elif valinta == "5":
            uusi_pelaaja = lataa_peli(paikat, kalat, "tallennus.json")

            if uusi_pelaaja is not None:
                pelaaja = uusi_pelaaja

        elif valinta == "6":
            print("Kiitos pelaamisesta!")
            break

        else:
            print("Väärä valinta.")


main()
