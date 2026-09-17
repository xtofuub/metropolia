def summa(lista):
    tulos = 0
    for luku in lista:
        tulos += luku
    return tulos


luvut = [1, 2, 3, 4, 5]
print("Listan summa:", summa(luvut))
