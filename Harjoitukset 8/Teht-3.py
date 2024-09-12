import mysql.connector
from geopy import distance

connection = mysql.connector.connect(host='localhost',
                                     database='flight_game',
                                     user='root',
                                     password='salasana',
                                     autocommit=True)

def lentoasema(koodi):
    koordinaatti = f"SELECT latitude_deg, longitude_deg from airport where ident = '{koodi}'"
    cursor = connection.cursor()
    cursor.execute(koordinaatti)
    result = cursor.fetchone()
    if result:
        return result
    else:
        print(f"Lentokenttää ICAO-koodilla {koodi} ei löytynyt.")
        return None


icao1 = input("Syötä ensimmäisen lentoaseman ICAO-koodi: ").strip().upper()
koordi1 = lentoasema(icao1)
icao2 = input("Syötä toisen lentoaseman ICAO-koodi: ").strip().upper()
koordi2 = lentoasema(icao2)

if koordi1 and koordi2:
    tulos = distance.distance(koordi1, koordi2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {tulos:.2f} km.")
else:
    print("Etäisyyden laskeminen epäonnistui, koska koordinaatteja ei löytynyt.")