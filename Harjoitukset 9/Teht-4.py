import random


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


def tulosta_autot(autot):
    print(f"{'Rekisteri':<10}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
    print("=" * 65)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<20}{auto.hetki_nopeus:<15}{auto.kuljettu_matka:<20}")


def kilpailu():
    autot = []

    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu_jatkuu = True

    while kilpailu_jatkuu:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kilpailu_jatkuu = False
                break
    tulosta_autot(autot)

kilpailu()
