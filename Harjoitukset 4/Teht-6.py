#Piin likiarvon laskeminen
#π≈4n/N, jossa n on yksikköympyrän sisälle sisälle tulevat pisteet, N on kaikki pisteet
#epäyhtälöllä x^2+y^2<1 testataan, onko yksittäinen piste ympyrän sisällä

import math
import random
iterator = 0
N = input("Kuinka monta pistettä haluat testata?: ")
N = int(N)
#kaikki pisteet jos haluaa kokeilla ilman käyttäjä inputtia
#N = 10000000
n = 0 #ympyrän sisälle osuvat pisteet
while iterator < N:
    iterator += 1
    #arvotaan koordinaatit liukulukuina väliltä 1, -1, kaksi erillaista tapaa:
    x = random.random() * 2 - 1
    y = random.uniform (-1,1)
    #print("Satunnainen piste: " + str(x) + ", " + str(y))
    #print(x**2 + y**2 <1)
    if x**2 + y**2 <1:
        #print("Osui ympyrän sisälle")
        n = n + 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle")
result = 4*n / N
print(f"Piin likiarvo on: {result}")
print(f"Virhe: {result- math.pi}")

