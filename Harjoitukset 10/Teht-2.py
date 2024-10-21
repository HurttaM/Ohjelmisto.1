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

class Talo:
    def __init__(self, alin, ylin, luku):
        self.hissit = [Hissi(alin, ylin) for i in range(luku)]

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if hissi_numero < 0 or hissi_numero >= len(self.hissit):
            print("Virhe: Hissin numero ei ole olemassa.")
            return

        hissi = self.hissit[hissi_numero]
        print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}.")
        hissi.siirry_kerrokseen(kohde_kerros)

talo = Talo(0, 10, 3)
talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 10)
talo.aja_hissia(0, 0)
