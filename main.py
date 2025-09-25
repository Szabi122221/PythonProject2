try:
    eredmeny = 10 / ertek
except ZeroDivisionError:
    print("Nullával való osztás nem lehetséges")
except NameError:
    print("Névhiba")
else:
    print(eredmeny)

