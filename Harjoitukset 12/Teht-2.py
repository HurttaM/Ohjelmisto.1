import requests
import json

def hae_saa(paikka):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikka}&units=metric&appid={'mysupersecretkey'}"

    try:
        vastaus = requests.get(url).json()

    except requests.exceptions.RequestException as e:
        print("Virhe. Verkko-ongelma")

    if vastaus.get("cod") != 200:
        virhekoodi = vastaus.get("cod")
        virheviesti = vastaus.get("message")
        print(f"Virhe ({virhekoodi}): {virheviesti}. Yritä uudelleen.")
        return

    saatila = vastaus["weather"][0]["description"]
    lampotila = vastaus["main"]["temp"]


    print(f"Säätila: {saatila}")
    print(f"Lämpötila: {lampotila:.2f} °C")


paikka = input("Anna kaupungin nimi: ")

hae_saa(paikka)