# adattípusok
''' Több soros megjegyzés
    még itt is tart '''

szoveg = 'autorendszam'
szam = 15
logikai = True

print(szoveg)
print(szam)

szam *=2
print(szam)
print(not logikai)
print(szam > 20)

print(szoveg[0])
print(szoveg[0:4])
print(szoveg[4:])
print(szoveg[4:8])
print(szoveg[-4:])

lista = ["habos", "kakao"]
print(lista[0]+lista[1])
print(lista[1]+lista[0])
lista += ["tejszines"]
print(lista)
print(lista[2]+lista[0]+lista[1])

halmaz = {5, 4, 8, 5}
print(halmaz)
halmaz |= {"alma"}
print(halmaz)

szotar = {"nev": "Bela", "kor": 43}
print(szotar)

eletkor = int(input("Kerem az eletkorat: "))
eletkor += 5
print(eletkor)
print(szotar["nev"], "kora:\n", eletkor, sep=" ", end="\n")

print("szoveg".rjust(50, "-"))
