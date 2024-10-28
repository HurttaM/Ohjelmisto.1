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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


def paohjelma():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.kiihdyta(120)
    polttomoottoriauto.kiihdyta(100)

    sähköauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauton ({sähköauto.rekisteritunnus}) kuljettu matka: {sähköauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus}) kuljettu matka: {polttomoottoriauto.kuljettu_matka} km")

paohjelma()