import random


def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = heita_noppaa(maksimi)
    print(silmaluku)

    if silmaluku == maksimi:
        break
