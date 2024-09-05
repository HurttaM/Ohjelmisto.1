from math import pi

def pizza (hal, eur):
    hinta = eur / (pi*(hal/2)**2)
    return hinta

koko1 = float(input("Anna ensimmäinsen pitsan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pitsan hinta: "))
koko2 = float(input("Anna toisen pitsan halkaisija: "))
hinta2 = float(input("Anna toisen pitsan hinta: "))

if pizza (koko1, hinta1) < pizza (koko2, hinta2):
    print("Ensimmäinen pitsa on halvempi")
elif pizza (koko2, hinta2) < pizza (koko1, hinta1):
    print("Toinen pitsa on halvempi")