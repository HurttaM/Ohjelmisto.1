#while True:
    #tuuma = float(input("Anna tuumat: "))
    #if tuuma < 0:
        #print("Virhe, anna positiivisia numeroita")
        #break
    #sentti = int(tuuma) * 2.54
    #print(f"{tuuma:.0f} tuumaa on {sentti:.2f} senttiä")

#ilman break komentoa:
tuuma = float(input("Anna tuumat: "))
while tuuma >= 0:
    sentti = tuuma * 2.54
    print(f"{tuuma:.0f} tuumaa on {sentti:.2f} senttiä")
    tuuma = float(input("Anna tuumat: "))
print("Virhe, anna positiivisia numeroita")