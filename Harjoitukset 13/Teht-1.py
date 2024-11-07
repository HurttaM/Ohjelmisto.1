from flask import Flask, jsonify

app = Flask(__name__)

def alkuluku(koko):
    if koko == 0 or koko == 1:
        return False
    elif koko > 1:
        for luku in range(2, koko):
            if koko % luku == 0:
                return False
        return True
    else:
        return False

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    vastaus = {
        "Number": luku,
        "isPrime": alkuluku(luku)
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)

