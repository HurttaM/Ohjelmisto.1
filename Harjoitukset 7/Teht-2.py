def nimet():
    nimet_set = set()

    while True:
        nimi = input("Anna nimi: ").strip().upper()
        if nimi == "":
            break

        if nimi in nimet_set:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet_set.add(nimi)
    for nimi in nimet_set:
        print(nimi)

nimet()