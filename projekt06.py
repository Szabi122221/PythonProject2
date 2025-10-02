import turtle
import projekt05

ablak = turtle.Screen()
ablak.title("Pontverseny")
ablak.bgcolor("black")

def kilepes():
    ablak.bye()

pont1 = projekt05.Mozgopont("cyan", -200, 0, 10)
pont2 = projekt05.Mozgopont("magenta", -200, 50, 10)
pont3 = projekt05.Mozgopont("yellow", -200, -50, 10)

ablak.listen()

ablak.onkey(pont1.inditas, "d")
ablak.onkey(pont2.inditas, "k")
ablak.onkey(pont3.inditas, "v")
ablak.onkey(kilepes, "Escape")

turtle.mainloop()