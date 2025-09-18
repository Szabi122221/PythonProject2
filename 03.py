egyik_szam = input("Kérek egy számot")
if egyik_szam.isdigit():
    egyik_szam = int(egyik_szam)
    if egyik_szam==0:
        print("Nem megfelelő szám")
    elif egyik_szam > 100:
        print("Túl nagy számot adtál meg")
    else:
        print("Megfelelő szám")
else:
    print("Nem számot adtál meg!")



# masik_szam = input("Kérek egy másik számot")