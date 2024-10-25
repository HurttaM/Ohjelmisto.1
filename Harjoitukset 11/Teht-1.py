class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumäärä: {self.sivumaara} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")

if __name__ == "__main__":
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()