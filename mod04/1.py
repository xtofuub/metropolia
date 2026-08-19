pituus = float(input("Anna kalan pituus cm: "))

if pituus < 37:
    alamitta = 37 - pituus
    print("Kalan pituus on alamittainen.")
    print("Alamittaa puuttuu", alamitta, "cm")
else:
    print("Kala ei ole alamittainen.")