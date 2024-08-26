vuosi = input("Mikä vuosi on?: ")
vuosi = int(vuosi)
if vuosi % 400 == 0:
    print(str(vuosi)+ " ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print(str(vuosi) + " on karkausvuosi")
else:
    print(str(vuosi)+ " ei ole karkausvuosi")