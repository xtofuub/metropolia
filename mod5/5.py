tunnus = "python"
salasana = "rules"
counter = 0
tunnus1 = str(input("Anna tunnus: "))
salasana1 = str(input("Anna salasana: "))

while tunnus1 != tunnus or salasana != salasana1:
    print(f"Pääsy evätty {counter} kertaa")
    tunnus1 = str(input("Anna tunnus: "))
    salasana1 = str(input("Anna salasana: "))
    counter = counter + 1
    if counter >= 5:
        print("mee vittuun")
        exit()
print("Tervetuloa")