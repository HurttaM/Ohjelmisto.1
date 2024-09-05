def gallion(määrä):
    litra = määrä * 3.785
    return litra

määrä = 0

while True:
    määrä = int(input("Anna gallonamäärä (muutetaan litroiksi): "))
    if määrä < 0:
        print("Anna vain positiivisia lukuja, ohjelma päättyy")
        break
    litrat = gallion(määrä)
    print(litrat)