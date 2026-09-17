# Projekti 3: Päävalikon toiminnot ja inventaario

inventaario = []


def lisaa_esine():
    """Kysyy pelaajalta esineen ja lisää sen inventaarioon."""
    esine = input("Mikä esine lisätään inventaarioon? ")
    inventaario.append(esine)
    print(f"{esine} lisättiin inventaarioon.")


def nayta_inventaario():
    """Tulostaa kaikki inventaariossa olevat esineet."""
    print("\n--- Inventaario ---")

    if len(inventaario) == 0:
        print("Inventaario on tyhjä.")
    else:
        for i, esine in enumerate(inventaario, 1):
            print(f"{i}. {esine}")


def tutki_aluetta():
    """Kertoo pelaajalle, mitä alueelta löytyy."""
    print("\nTutkit aluetta...")
    print("Löydät vanhan oven ja pienen laatikon.")


def lopeta_peli():
    """Lopettaa pelin."""
    print("Peli lopetetaan. Kiitos pelaamisesta!")


def paavalikko():
    """Näyttää päävalikon ja suorittaa valitun toiminnon."""
    while True:
        print("\n=== PÄÄVALIKKO ===")
        print("1. Lisää esine inventaarioon")
        print("2. Näytä inventaario")
        print("3. Tutki aluetta")
        print("4. Lopeta peli")

        valinta = input("Valitse toiminto (1-4): ")

        if valinta == "1":
            lisaa_esine()
        elif valinta == "2":
            nayta_inventaario()
        elif valinta == "3":
            tutki_aluetta()
        elif valinta == "4":
            lopeta_peli()
            break
        else:
            print("Virheellinen valinta. Valitse numero 1-4.")


paavalikko()
