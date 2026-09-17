lentoasemat = {}

while True:
    print("\n1 - Syötä uusi lentoasema")
    print("2 - Hae lentoasema")
    print("3 - Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")
    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta.")
