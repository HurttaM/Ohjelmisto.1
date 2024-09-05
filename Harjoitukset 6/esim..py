
#print([1,5,3].sort())

#def do_something():
    #print("Tämä aliohjelma tekee!")
    #print("Ja voi tehdä enemmänkin!")
    # return ei ole välttämätön, ilman sitä paluuarvo None
    #return "Tämä on funktion palauttama merkkijono"
    #pass, kertoo, että koodinpätkässä ei ole mitään sisällä

#return_value = do_something()
#print(return_value)

#funktio, jolla parametreja (argumentteja)
#parametri muuttuja on käytössä vain funktion sisällä
#def say_hello(to):
    #print("Moi " + to)
    #return "Moi " + to

#say_hello("Matti") # "Moi Matti"
#print(say_hello("Matti"))

#useampi parametri ja useampi arvo palautetaan listana
def create_greetings(to, count):
    greetings = []
    for i in range(1, count +1):
        #print(f"{i}. kerran Moi " + to)
        greetings.append(f"{i}. kerran Moi " + to)
        return greetings

greetings = create_greetings("Jorma", 3)
print(greetings)
#listan kaikkien arvojen käsittely for silmukalla
for i in range(len(greetings)):
    print(greetings[i])
for greeting in greetings:
    print(greeting)