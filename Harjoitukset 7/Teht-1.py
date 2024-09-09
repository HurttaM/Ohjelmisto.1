vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "syksy", "syksy", "syksy")
kknumero = int(input("Anna kuukauden numero (1-12): "))
vuodenaika = vuodenajat[kknumero-1]
print (f"{kknumero}. vuodenaika on {vuodenaika}.")