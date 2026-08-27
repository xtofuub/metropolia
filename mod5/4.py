import random
oikee = random.randint(1, 10) 

while True:
    arvaus = float(input("Anna numero 1-10: "))
    if arvaus == oikee:
        print("oikein")
        break
    elif arvaus > oikee:
        print("liian iso")
    elif arvaus < oikee:
        print("liian pieni")