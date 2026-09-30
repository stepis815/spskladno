cislo1 = float(input("Zadej první číslo 1:"))
cislo2 = float(input("Zadej druhé číslo 2:"))

print("Součet: ", cislo1+cislo2)
print("DeSoučet: ", cislo1-cislo2)
print("Součin: ", cislo1*cislo2)
print("DeSoučin: ", cislo1/cislo2)





pozice = str(input("Kde se nacházíš? (dalnice, mimo_obec, obec)"))
rychlost = int(input("Jak rychle jedeš?"))

if pozice == "dalnice":
    if rychlost <= 130:
        print("OK")
    else:
        print("Vysoká rychlost!")
elif pozice == "mimo_obec":
    if rychlost <= 90:
        print("OK")
    else:
        print("Vysoká rychlost!")
elif pozice == "obec":
    if rychlost <= 50:
        print("OK")
    else:
        print("Vysoká rychlost!")