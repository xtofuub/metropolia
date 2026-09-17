import random

koodi1 = ""
koodi2 = ""

for i in range(3):
    koodi1 += str(random.randint(0, 9))

for i in range(4):
    koodi2 += str(random.randint(1, 6))

print("Kolmenumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)