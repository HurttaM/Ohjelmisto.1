sk = input("Sukupuoli?: ")
hg = input("Hemoglobiini?: ")
if sk == "Nainen":
    if int(hg) < 117:
        print("Hemoglobiinisi on liian alhainen")
    elif 117 >= int(hg) <= 175:
        print("Hemoglobiinisi on normaali")
    elif int(hg) > 175:
        print("Hemoglobiinisi on liian korkea")
elif sk == "Mies":
    if int(hg) < 134:
        print("Hemoglobiinisi on liian alhainen")
    elif 134 >= int(hg) <= 195:
        print("Hemoglobiinisi on normaali")
    elif int(hg) > 195:
        print("Hemoglobiinisi on liian korkea")
