inventaario = []


def lisaa_esine():
    esine = input("Anna esine: ")
    inventaario.append(esine)
    print("Esine lisätty inventaarioon.")


def nayta_inventaario():
    if len(inventaario) == 0:
        print("Inventaario on tyhjä.")
    else:
        print("Inventaario:")
        for esine in inventaario:
            print(esine)


def pelaa():
    print("Pelaat peliä.")


while True:
    print("\nPäävalikko")
    print("1 - Lisää esine")
    print("2 - Näytä inventaario")
    print("3 - Pelaa")
    print("4 - Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        lisaa_esine()
    elif valinta == "2":
        nayta_inventaario()
    elif valinta == "3":
        pelaa()
    elif valinta == "4":
        break
    else:
        print("Virheellinen valinta.")
