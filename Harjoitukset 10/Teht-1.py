class Hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.kerros = alin


    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            print("Virhe: Kerros on hissin rajojen ulkopuolella.")
            return

        while self.kerros < kohde_kerros:
            self.kerros_ylos()

        while self.kerros > kohde_kerros:
            self.kerros_alas()

hissi = Hissi(5, 0)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(0)