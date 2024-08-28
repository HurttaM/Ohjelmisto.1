koko = int(input("Anna kokonaisluku: "))
if koko == 0 or koko == 1:
    print("Antamasi luku ei ole alkuluku")
elif koko > 1:
    for luku in range (2,koko):
        if (koko % luku) == 0:
            print("Antamasi luku ei ole alkuluku")
            break
    else:
        print("Antamasi luku on alkuluku")
else:
    print("Antamasi luku ei ole alkuluku")