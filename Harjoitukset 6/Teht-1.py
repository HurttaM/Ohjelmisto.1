import random

def nopanheitto():
    heitto = random.randint(1,6)
    return heitto

arvo = 0

while arvo != 6:
    arvo = nopanheitto()
    print(arvo)