lista = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        lista.sort()
        print ("Pienin lukusi oli " + str(lista[0]) + " ja suurin lukusi oli " + str(lista[len(lista) - 1]))
        break
    luku = int(luku)
    lista.append(luku)
