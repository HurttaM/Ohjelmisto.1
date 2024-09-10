import mysql.connector

# "tallennetaan" connect-funktion palauttama yhteys muuttujaan jatkokäyttöä varten
connection = mysql.connector.connect(host='localhost',
                                     database='flight_game',
                                     user='root',
                                     password='salasana',
                                     autocommit=True)


cursor = connection.cursor()
cursor.execute("SELECT name, iso_country FROM country")
result = cursor.fetchone()
print(result)
#fetchmany() palauttaa n seuraavaa osoittimen kohdalta
#result = cursor.fetchmany(3)
#print(result)
#fetchall() palauttaa kaikki (loput)
result = cursor.fetchall()
#juuri haettiin tulosrivien lukumäärä
print (cursor.rowcount)
print(result)
for row in result:
    print(f"Maan {row[0]} maakoodi on {row[1]}.")
print (f"Maita on yhteensä: {cursor.rowcount}")
if cursor.rowcount == 0:
    print("Ei yhtään maata")

