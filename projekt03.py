def szam_bekerese(legnagyobb_szam):
    szam = input("Kérek egy számot: ")
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

def szamologep():
    muvelet = input("Milyen műveletet akar végrehajtani? (+,-,*,/): ")
    egyik_szam = szam_bekerese(10)
    masik_szam = szam_bekerese(100)
    if muvelet == "+":
        eredmeny = egyik_szam + masik_szam
    elif muvelet == "-":
        eredmeny = egyik_szam - masik_szam
    elif muvelet == "*":
        eredmeny = egyik_szam * masik_szam
    elif muvelet == "/":
        eredmeny = egyik_szam / masik_szam
    else:
        print("Nem megfelelő művelet!")

    print(f"Az eredmény: {egyik_szam} {muvelet} {masik_szam} = {eredmeny}")

def veletlenszam():
    import random
    szam = random.randint(1, max)
    return szam

def egesz_szam_bekerese():
    while True:
        szam = input("Kérek egy egész számot: ")
        try:
            szam = int(szam)
            break
        except ValueError:
            print("Nem egész számot adott meg!!")
    return szam


# program indítása
if __name__ == "__main__":
    print(egesz_szam_bekerese())