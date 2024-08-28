max_yritykset = 5
yritykset = 0

while True:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    elif tunnus != "python" or salasana != "rules":
        yritykset +=1
        print("Väärä tunnus tai salasana")
        if yritykset == max_yritykset:
            print ("Pääsy evätty")
            break
        