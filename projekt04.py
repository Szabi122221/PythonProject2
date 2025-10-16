def negyszog(a, b):
    ker = 2 * a + 2 * b
    ter = a * b
    alakzat = "téglalap"
    if a == b:
        alakzat = "négyzet"
    return ker, ter, alakzat

def osszegzes(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg, legnagyobb

if __name__ == "__main__":
    sorozat = [1,2,"három",4,5]
    for elem in sorozat:
        print(elem)

for i in range(1, 10):
    print(i)

for _ in range(100):
    print("Nem leszek rossz!")


print("Összeg:", osszegzes(1, 2, 3, 4, 5)[0])
print("A legnagyobb érték:", osszegzes(1, 2, 3, 4, 5)[1])

eredmeny = negyszog(4, 4)
print ("Kerület:", eredmeny[0])
print ("Terület:", eredmeny[1])
print ("Alakzat:", eredmeny[2])