class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetki_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä (self, muutos):
        uusi_nopeus = self.hetki_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.hetki_nopeus = self.huippunopeus
            print(f"Auton huippunopeus saavutettu: {auto1.hetki_nopeus} km/h")
        elif uusi_nopeus < 0:
            self.hetki_nopeus = 0
            print(f"Auto pysähtyi. Nopeus: {auto1.hetki_nopeus} km/h")
        else:
            self.hetki_nopeus = uusi_nopeus
            print(f"Tämänhetkinen nopeus: {auto1.hetki_nopeus} km/h")

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-200)