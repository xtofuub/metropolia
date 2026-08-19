hytti = input("Anna hytti (LUX, A, B, C): ")

if hytti == "LUX":
    print("parvekkeellinen hytti yläkannella.")

elif hytti == "A":
    print("ikkunallinen hytti autokannen yläpuolella.")

elif hytti == "B":
    print("ikkunaton hytti autokannen yläpuolella.")

elif hytti == "C":
    print("ikkunaton hytti autokannen alapuolella.")

else:
    print("Tuntematon hyttiluokka.")