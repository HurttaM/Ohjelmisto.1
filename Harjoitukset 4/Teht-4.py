import random
oikea = random.randint(1,10)
while True:
    arvaus = input("Arvaa luku 1 ja 10 välillä: ")
    arvaus = float(arvaus)
    if arvaus < oikea:
        print("Liian pieni luku")
    elif arvaus > oikea:
        print("Liian suuri luku")
    elif arvaus == oikea:
        print("Juuri näin! Oikea luku oli " + str(oikea))
        break