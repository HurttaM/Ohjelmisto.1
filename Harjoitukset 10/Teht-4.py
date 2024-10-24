import random


# Auto-luokka aiemmasta tehtävästä
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetki_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.hetki_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.hetki_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.hetki_nopeus = 0
        else:
            self.hetki_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        kuljettu = self.hetki_nopeus * tunnit
        self.kuljettu_matka += kuljettu


# Kilpailu-luokka
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<12}{'Huippunopeus (km/h)':<22}{'Nopeus (km/h)':<16}{'Kuljettu matka (km)':<20}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<22}{auto.hetki_nopeus:<16}{auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
def paohjelma():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    print(f"Kilpailun nimi: {kilpailu.nimi}")

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            print(f"\nTunti {tunti}: Tilannekatsaus")
            kilpailu.tulosta_tilanne()

    print("\nKilpailu päättyi!")
    kilpailu.tulosta_tilanne()

paohjelma()