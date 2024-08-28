import random
summa = 0
noppia = int(input("Kuinka monta noppaa?: "))
for luku in range(noppia):
    heitto = random.randint(1,6)
    summa +=heitto
print(f"Noppien silmälukujen summa on: {summa}")