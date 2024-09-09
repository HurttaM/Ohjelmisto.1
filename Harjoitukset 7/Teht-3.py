def lentoasema():
    asemat = {}

    while True:
        teko = input("Haluatko syöttää lentoaseman, hakea jo syötetyn lentoaseman vai lopettaa? (syöttää/hakea/lopettaa): ").strip().lower()

        if teko == "lopettaa":
            print("Ohjelma lopetetaan.")
            break

        elif teko == "syöttää":
            icao = input("Syötä aseman ICAO-koodi: ").strip().upper()
            nimi = input("Syötä lentoaseman nimi: ").strip()
            if icao in asemat:
                print(f"Lentoasema {icao} on jo olemassa nimellä {asemat[icao]}.")
            else:
                asemat[icao] = nimi
                print(f"Lentoasema {icao} ({nimi}) tallennettu.")

        elif teko == "hakea":
            icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").strip().upper()
            if icao in asemat:
                print(f"Lentoaseman {icao} nimi on {asemat[icao]}.")
            else:
                print(f"Lentoasemaa ICAO-koodilla {icao} ei löytynyt.")

        else:
            print("Virheellinen valinta. Yritä uudelleen.")

lentoasema()