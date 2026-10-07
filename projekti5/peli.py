def lue_tiedosto(tiedostonimi):
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()


intro = lue_tiedosto("intro.txt")
ohjeet = lue_tiedosto("instructions.txt")

print(intro)
print()
print(ohjeet)