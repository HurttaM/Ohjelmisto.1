koko = [4, 5, 299, 47, 36, 5, 573, 2856]

def kokonaisluvut(luku):
    lista = []
    for i in luku:
        if i % 2 == 0:
            lista.append(i)
    return lista

print(kokonaisluvut(koko))
print(koko)