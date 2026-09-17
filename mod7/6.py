import math


def yksikkohinta(diametri, hinta):
    sade = diametri / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala


diametri1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
diametri2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

hinta1_m2 = yksikkohinta(diametri1, hinta1)
hinta2_m2 = yksikkohinta(diametri2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {hinta1_m2:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {hinta2_m2:.2f} €/m²")

if hinta1_m2 < hinta2_m2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif hinta2_m2 < hinta1_m2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat antavat saman vastineen rahalle.")
