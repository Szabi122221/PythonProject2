def szam_bekerese(legnagyobb_szam):
    szam = input("Kérek egy számot")
    if szam.isdigit():
        szam = int(szam)
        if szam==0:
            print("Nem megfelelő szám")
        elif szam > legnagyobb_szam:
            print("Túl nagy számot adtál meg")
        else:
            print("Megfelelő szám")
    else:
        print("Nem számot adtál meg!")
    return szam

# Program indítás
egyik_szam = szam_bekerese(10)
print(egyik_szam)
masik_szam = szam_bekerese(100)
print(masik_szam)


# masik_szam = input("Kérek egy másik számot")