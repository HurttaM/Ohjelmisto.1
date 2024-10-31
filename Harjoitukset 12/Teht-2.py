import requests
import json

def hae_saa(paikka):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikka}&units=metric&appid={'37922119c8b329ff65c9c70a23c7b3ae'}"
    vastaus = requests.get(url).json()

    if vastaus.get("cod") != 200:
        virhekoodi = vastaus.get("cod")
        virheviesti = vastaus.get("message", "Tuntematon virhe")
        print(f"Virhe ({virhekoodi}): {virheviesti}. Yritä uudelleen.")
        return

    saatila = vastaus["weather"][0]["description"]
    lampotila = vastaus["main"]["temp"]


    print(f"Säätila: {saatila}")
    print(f"Lämpötila: {lampotila:.2f} °C")


paikka = input("Anna kaupungin nimi: ")

hae_saa(paikka)