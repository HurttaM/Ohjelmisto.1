
#def kokonaisluvut(eka, toka, kolmas, neljas, viides):
    #summa = eka + toka + kolmas + neljas + viides
    #return summa

#luku1 = float(input("Anna ensimmäinen kokonaisluku: "))
#luku2 = float(input("Anna toinen kokonaisluku: "))
#luku3 = float(input("Anna kolmas kokonaisluku: "))
#luku4 = float(input("Anna neljäs kokonaisluku: "))
#luku5 = float(input("Anna viides kokonaisluku: "))
#tulos = kokonaisluvut(luku1, luku2, luku3, luku4, luku5)
#print("Kokonaislukujen tulos: " +str(tulos))

koko = [4, 5, 299, 47, 36, 5, 573, 2856]

def kokonaisluvut(luku):
    sum = 0
    for i in luku:
        sum += i
    return sum

print(kokonaisluvut(koko))

