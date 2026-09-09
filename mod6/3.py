luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    alkuluku = False
else:
    alkuluku = True

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")
