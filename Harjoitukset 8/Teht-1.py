import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='flight_game',
                                     user='root',
                                     password='salasana',
                                     autocommit=True)

def lentoasema(koodi):
    sql = f"SELECT name, iso_country FROM airport where ident = '{koodi}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"Lentoaseman {row[0]} maakoodi on {row[1]}.")


icao = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
lentoasema(icao)

