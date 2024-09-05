import random


def nopanheitto(count):
    heitto = random.randint(1,count)
    return heitto

arvo = 0

tahko = input("Anna tahkojan lukumäärä: ")

while arvo != int(tahko):
    arvo = nopanheitto(int(tahko))
    print(arvo)