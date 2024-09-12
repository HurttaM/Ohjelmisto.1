import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='flight_game',
                                     user='root',
                                     password='salasana',
                                     autocommit=True)

def lentoasema(koodi):
    type = f"SELECT type, COUNT(*) AS count FROM airport WHERE iso_country = '{koodi}' GROUP BY type;"
    cursor = connection.cursor()
    cursor.execute(type)
    result = cursor.fetchall()
    return result

maa = input("Syötä lentoaseman maakoodi: ").strip().upper()
lentoasema(maa)
print(lentoasema(maa))