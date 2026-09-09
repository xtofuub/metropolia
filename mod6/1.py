import random

maara = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

for _ in range(maara):
    summa += random.randint(1, 6)

print(f"Silmälukujen summa: {summa}")
