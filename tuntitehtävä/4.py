vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0:
    print("Vuosi on olympia vuosi.")
elif vuosi == 2020:
    print("Vuosi ei ole olympia vuosi.")
elif vuosi == 2021:
    print("Vuosi on olympia vuosi.")
else:
    print("Vuosi ei ole olympia vuosi.")