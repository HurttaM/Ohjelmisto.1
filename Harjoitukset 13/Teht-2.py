from flask import Flask, jsonify, Response
import mysql.connector
import json

app = Flask(__name__)

connection = mysql.connector.connect(
    host='localhost',
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)


def get_airport_info(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    if result:
        return {
            "ICAO": icao_code,
            "Name": result[0],
            "Municipality": result[1]
        }
    else:
        return None


@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def airport_info(icao_code):
    airport_data = get_airport_info(icao_code.upper())

    if airport_data:
        return jsonify(airport_data)
    else:
        return Response(json.dumps({"error": "Airport not found"}), status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)