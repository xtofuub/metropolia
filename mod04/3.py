sukupuoli = input("Anna sukupuoli (n/m): ")
if sukupuoli == "m":
    hemoglobiini = input("Anna hemoglobiiniarvo:")
    if 134 <= float(hemoglobiini) <= 195:
        print("Olet mies ja hemoglobiiniarvo on normaali.")
    elif float(hemoglobiini) < 134:
        print("Olet mies ja hemoglobiiniarvo on alhainen.")
    elif float(hemoglobiini) > 195:
        print("Olet mies ja hemoglobiiniarvo on korkea.")
    else:
        print("Virheellinen hemoglobiiniarvo.")
elif sukupuoli == "n":
    hemoglobiini= input("Anna hemoglobiiniarvo:")
    if 117 <= float(hemoglobiini) <= 175:
        print("Olet nainen ja hemoglobiiniarvo on normaali.")
    elif float(hemoglobiini) < 117:
        print("Olet nainen ja hemoglobiiniarvo on alhainen.")
    elif float(hemoglobiini) > 175:
        print("Olet nainen ja hemoglobiiniarvo on korkea.")
    else:
        print("Virheellinen hemoglobiiniarvo.")
else:
    print("Virheellinen sukupuoli.")