leiviskä = input("Kuinka monta leivisköä? ")
naula = input("Kuinka monta naulaa? ")
luoti = input("Kuinka monta luotia? ")
luotiN = float(luoti) * 13.3
naulaN = float(naula) * 13.3 * 32
leiviskäN = float(leiviskä) * 20 * 32 * 13.3
sum = float (luotiN) + float (naulaN) + float (leiviskäN)
kilo = int(sum // 1000)
gramma = sum - kilo * 1000
print(f"Paino on {kilo} kiloa ja {gramma:.2f} grammaa.")
