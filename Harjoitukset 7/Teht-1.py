vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kknumero = int(input("Anna kuukauden numero (1-12): "))
vuodenaika = vuodenajat[kknumero-1]
print (f"{kknumero}. vuodenaika on {vuodenaika}.")