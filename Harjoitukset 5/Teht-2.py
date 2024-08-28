lista = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        lista.sort(reverse=True)
        print(lista)
        break
    lista.append(luku)