zbozi = ["NVIDIA RTX 3060", "NVIDIA RTX 3070", "NVIDIA RTX 3070Ti", "NVIDIA RTX 3080", "NVIDIA RTX 3080Ti", "NVIDIA RTX 3090", "NVIDIA RTX 4060"]
kosik = []
print("----------------------------")
print("Vítejte v našem obchodě!")
print("----------------------------")

def zbozi1 ():
    print ("----------------------------")
    print("Zde je zboží:")
    print(" ")
    print("----------------------------")

def kosik1 ():
    print ("----------------------------")
    print (" ")
    print("Zde je košík:")
    print (" ")
    print("----------------------------")

def pole1(pole):
    for x in range(len(pole)):
        print(f"0{x+1}: {pole[x]}")
    print(" ")
    print("----------------------------")
while(True):
    zbozi1()
    pole1(zbozi)

    vyber = int(input("Číslo zvoleného produktu: "))

    if 0<vyber<=len(zbozi):
        kosik.append(zbozi[vyber]) # přidává na konec prvek
        kosik1()
        pole1(kosik)
        zbozi.pop(vyber) # odstraní poslední prvek a vrátí ji zpátky


